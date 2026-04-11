import { useState, useEffect, useMemo, useRef } from "react";
import { useSearchParams, useNavigate } from "react-router";
import { Tabs, Card, Chip, SelectField, EmptyState } from "./ui";
import { teams, getTeamIdByName, type Team } from "../data";
import { GitBranch } from "lucide-react";

export function DependenciesPage() {
  const [searchParams] = useSearchParams();
  const navigate = useNavigate();
  const focusTeamName = searchParams.get("focus") || "";

  const [tab, setTab] = useState("graph");
  const [selectedTeam, setSelectedTeam] = useState(focusTeamName || teams[0].name);
  const [direction, setDirection] = useState<"both" | "upstream" | "downstream">("both");
  const [depth, setDepth] = useState<1 | 2>(1);

  useEffect(() => {
    if (focusTeamName) setSelectedTeam(focusTeamName);
  }, [focusTeamName]);

  const teamOptions = teams.map((t) => ({ value: t.name, label: t.name })).sort((a, b) => a.label.localeCompare(b.label));

  // Compute visible nodes
  const { nodes, edges } = useMemo(() => {
    const center = teams.find((t) => t.name === selectedTeam);
    if (!center) return { nodes: [], edges: [] };

    const nodeSet = new Set<string>();
    const edgeList: { from: string; to: string }[] = [];
    nodeSet.add(center.name);

    const addDeps = (teamName: string, currentDepth: number) => {
      const t = teams.find((tm) => tm.name === teamName);
      if (!t) return;
      if (direction !== "downstream") {
        t.upstream.forEach((u) => {
          if (!nodeSet.has(u)) {
            nodeSet.add(u);
            if (currentDepth < depth) addDeps(u, currentDepth + 1);
          }
          edgeList.push({ from: u, to: teamName });
        });
      }
      if (direction !== "upstream") {
        t.downstream.forEach((d) => {
          if (!nodeSet.has(d)) {
            nodeSet.add(d);
            if (currentDepth < depth) addDeps(d, currentDepth + 1);
          }
          edgeList.push({ from: teamName, to: d });
        });
      }
    };

    addDeps(center.name, 1);

    // Remove duplicate edges
    const uniqueEdges = edgeList.filter((e, i, arr) =>
      arr.findIndex((x) => x.from === e.from && x.to === e.to) === i
    );

    return { nodes: Array.from(nodeSet), edges: uniqueEdges };
  }, [selectedTeam, direction, depth]);

  return (
    <div className="space-y-4">
      <h1>Dependencies</h1>
      <Tabs
        tabs={[
          { key: "graph", label: "Graph View" },
          { key: "list", label: "List View" },
        ]}
        active={tab}
        onChange={setTab}
      />

      {/* Controls */}
      <div className="flex items-end gap-4 mt-4">
        <SelectField
          label="Focus team"
          value={selectedTeam}
          onChange={setSelectedTeam}
          options={teamOptions}
          className="w-[250px]"
        />
        <SelectField
          label="Direction"
          value={direction}
          onChange={(v) => setDirection(v as any)}
          options={[
            { value: "both", label: "Both" },
            { value: "upstream", label: "Upstream only" },
            { value: "downstream", label: "Downstream only" },
          ]}
          className="w-[160px]"
        />
        <SelectField
          label="Depth"
          value={String(depth)}
          onChange={(v) => setDepth(Number(v) as 1 | 2)}
          options={[
            { value: "1", label: "1 level" },
            { value: "2", label: "2 levels" },
          ]}
          className="w-[120px]"
        />
      </div>

      {tab === "graph" && <GraphView nodes={nodes} edges={edges} center={selectedTeam} navigate={navigate} />}
      {tab === "list" && <ListView selectedTeam={selectedTeam} navigate={navigate} />}
    </div>
  );
}

// Simple SVG graph
function GraphView({
  nodes, edges, center, navigate,
}: {
  nodes: string[]; edges: { from: string; to: string }[];
  center: string; navigate: (path: string) => void;
}) {
  if (nodes.length <= 1 && edges.length === 0) {
    return <EmptyState title="No dependencies to show" description="This team has no dependencies in the selected direction." icon={<GitBranch size={40} />} />;
  }

  // Layout: center node in middle, upstream left, downstream right
  const centerTeam = teams.find((t) => t.name === center);
  const upstreamNodes = nodes.filter((n) => n !== center && edges.some((e) => e.to === center && e.from === n));
  const downstreamNodes = nodes.filter((n) => n !== center && edges.some((e) => e.from === center && e.to === n));
  const otherNodes = nodes.filter((n) => n !== center && !upstreamNodes.includes(n) && !downstreamNodes.includes(n));

  // Assign positions
  const nodePositions: Record<string, { x: number; y: number }> = {};
  const svgWidth = 900;
  const colX = [120, 450, 780];

  const layoutColumn = (names: string[], x: number) => {
    const spacing = Math.min(60, 500 / Math.max(names.length, 1));
    const startY = Math.max(30, 250 - (names.length * spacing) / 2);
    names.forEach((name, i) => {
      nodePositions[name] = { x, y: startY + i * spacing };
    });
  };

  layoutColumn(upstreamNodes, colX[0]);
  nodePositions[center] = { x: colX[1], y: 250 };
  layoutColumn(downstreamNodes, colX[2]);
  // Others spread around
  otherNodes.forEach((n, i) => {
    const isUp = edges.some((e) => e.to !== center && e.from === n);
    const col = isUp ? colX[0] : colX[2];
    if (!nodePositions[n]) {
      const existingInCol = Object.values(nodePositions).filter(p => Math.abs(p.x - col) < 10);
      nodePositions[n] = { x: col, y: 30 + existingInCol.length * 55 };
    }
  });

  // Ensure all nodes have positions
  nodes.forEach((n) => {
    if (!nodePositions[n]) {
      nodePositions[n] = { x: 450, y: 30 + nodes.indexOf(n) * 50 };
    }
  });

  const maxY = Math.max(...Object.values(nodePositions).map((p) => p.y)) + 60;
  const svgHeight = Math.max(maxY, 300);

  return (
    <Card className="overflow-x-auto">
      {/* Legend */}
      <div className="flex items-center gap-4 mb-3 text-[12px] text-muted-foreground">
        <span className="flex items-center gap-1"><span className="w-3 h-3 rounded bg-primary inline-block" /> Focus team</span>
        <span className="flex items-center gap-1"><span className="w-3 h-3 rounded bg-purple-200 inline-block" /> Upstream</span>
        <span className="flex items-center gap-1"><span className="w-3 h-3 rounded bg-orange-200 inline-block" /> Downstream</span>
        <span className="flex items-center gap-1"><span className="w-8 border-t-2 border-muted-foreground inline-block" /> → Dependency direction</span>
      </div>
      <svg width={svgWidth} height={svgHeight} className="min-w-[900px]">
        <defs>
          <marker id="arrow" viewBox="0 0 10 7" refX="10" refY="3.5" markerWidth="8" markerHeight="6" orient="auto-start-reverse">
            <polygon points="0 0, 10 3.5, 0 7" fill="#999" />
          </marker>
        </defs>
        {/* Edges */}
        {edges.map((e, i) => {
          const from = nodePositions[e.from];
          const to = nodePositions[e.to];
          if (!from || !to) return null;
          return (
            <line
              key={i}
              x1={from.x + 70}
              y1={from.y + 15}
              x2={to.x - 5}
              y2={to.y + 15}
              stroke="#ccc"
              strokeWidth={1.5}
              markerEnd="url(#arrow)"
            />
          );
        })}
        {/* Nodes */}
        {nodes.map((name) => {
          const pos = nodePositions[name];
          if (!pos) return null;
          const isCenter = name === center;
          const isUpstream = upstreamNodes.includes(name);
          const fill = isCenter ? "#030213" : isUpstream ? "#ede9fe" : "#fff7ed";
          const textColor = isCenter ? "white" : "#333";
          const stroke = isCenter ? "#030213" : isUpstream ? "#c4b5fd" : "#fed7aa";
          return (
            <g
              key={name}
              className="cursor-pointer"
              onClick={() => navigate(`/teams/${getTeamIdByName(name)}`)}
            >
              <rect
                x={pos.x - 5}
                y={pos.y}
                width={150}
                height={30}
                rx={6}
                fill={fill}
                stroke={stroke}
                strokeWidth={1.5}
              />
              <text
                x={pos.x + 70}
                y={pos.y + 19}
                textAnchor="middle"
                fill={textColor}
                fontSize={11}
              >
                {name.length > 20 ? name.slice(0, 18) + "..." : name}
              </text>
            </g>
          );
        })}
      </svg>
    </Card>
  );
}

function ListView({ selectedTeam, navigate }: { selectedTeam: string; navigate: (path: string) => void }) {
  const team = teams.find((t) => t.name === selectedTeam);
  if (!team) return null;

  return (
    <div className="grid grid-cols-2 gap-4 mt-2">
      <Card>
        <h4 className="mb-3">Upstream Dependencies ({team.upstream.length})</h4>
        {team.upstream.length === 0 ? (
          <EmptyState title="No upstream dependencies" />
        ) : (
          <div className="space-y-2">
            {team.upstream.map((name) => {
              const t = teams.find((tm) => tm.name === name);
              return (
                <div
                  key={name}
                  className="flex items-center justify-between p-2 border border-border rounded-lg hover:bg-accent/50 cursor-pointer"
                  onClick={() => navigate(`/teams/${getTeamIdByName(name)}`)}
                >
                  <div>
                    <div className="text-[14px]">{name}</div>
                    {t && <div className="text-[12px] text-muted-foreground">{t.department} · {t.lead}</div>}
                  </div>
                  <Chip variant="upstream">Upstream</Chip>
                </div>
              );
            })}
          </div>
        )}
      </Card>
      <Card>
        <h4 className="mb-3">Downstream Dependencies ({team.downstream.length})</h4>
        {team.downstream.length === 0 ? (
          <EmptyState title="No downstream dependencies" />
        ) : (
          <div className="space-y-2">
            {team.downstream.map((name) => {
              const t = teams.find((tm) => tm.name === name);
              return (
                <div
                  key={name}
                  className="flex items-center justify-between p-2 border border-border rounded-lg hover:bg-accent/50 cursor-pointer"
                  onClick={() => navigate(`/teams/${getTeamIdByName(name)}`)}
                >
                  <div>
                    <div className="text-[14px]">{name}</div>
                    {t && <div className="text-[12px] text-muted-foreground">{t.department} · {t.lead}</div>}
                  </div>
                  <Chip variant="downstream">Downstream</Chip>
                </div>
              );
            })}
          </div>
        )}
      </Card>
    </div>
  );
}
