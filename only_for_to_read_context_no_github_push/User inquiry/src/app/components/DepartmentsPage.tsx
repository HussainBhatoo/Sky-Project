import { useState } from "react";
import { useNavigate } from "react-router";
import { Users, ChevronRight } from "lucide-react";
import { Card, Chip, StatusChip, Tabs } from "./ui";
import { departments, teams, getTeamById, type Team } from "../data";

export function DepartmentsPage() {
  const navigate = useNavigate();
  const [tab, setTab] = useState("list");

  const getTeamsForDept = (dept: typeof departments[0]) =>
    dept.teamIds.map((id) => getTeamById(id)).filter(Boolean) as Team[];

  return (
    <div className="space-y-4">
      <h1>Departments & Organisation</h1>
      <Tabs
        tabs={[
          { key: "list", label: "Departments" },
          { key: "org", label: "Org Chart" },
        ]}
        active={tab}
        onChange={setTab}
      />

      {tab === "list" && (
        <div className="space-y-6 mt-4">
          {departments.map((dept) => {
            const deptTeams = getTeamsForDept(dept);
            return (
              <Card key={dept.name}>
                <div className="flex items-center justify-between mb-3">
                  <div>
                    <h3>{dept.name}</h3>
                    <p className="text-[13px] text-muted-foreground">
                      Head{dept.heads.length > 1 ? "s" : ""}: {dept.heads.join(", ")}
                    </p>
                  </div>
                  <Chip variant="department">
                    <Users size={12} /> {deptTeams.length} teams
                  </Chip>
                </div>
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-3">
                  {deptTeams.map((team) => (
                    <div
                      key={team.id}
                      className="border border-border rounded-lg p-3 hover:bg-accent/50 cursor-pointer transition-colors"
                      onClick={() => navigate(`/teams/${team.id}`)}
                    >
                      <div className="flex items-center justify-between mb-1">
                        <span className="text-[14px]">{team.name}</span>
                        <StatusChip status={team.status} />
                      </div>
                      <span className="text-[12px] text-muted-foreground">Lead: {team.lead}</span>
                    </div>
                  ))}
                </div>
              </Card>
            );
          })}
        </div>
      )}

      {tab === "org" && (
        <div className="mt-4 space-y-4">
          {departments.map((dept) => {
            const deptTeams = getTeamsForDept(dept);
            return (
              <Card key={dept.name}>
                <div className="flex items-start gap-4">
                  {/* Dept node */}
                  <div className="flex flex-col items-center shrink-0">
                    <div className="bg-blue-100 text-blue-800 px-4 py-2 rounded-lg text-[14px] text-center min-w-[120px]">
                      <div>{dept.name}</div>
                      <div className="text-[11px] mt-0.5">{dept.heads.join(", ")}</div>
                    </div>
                  </div>
                  {/* Arrow */}
                  <div className="flex items-center pt-3">
                    <ChevronRight size={20} className="text-muted-foreground" />
                  </div>
                  {/* Teams */}
                  <div className="flex flex-wrap gap-2 pt-1">
                    {deptTeams.map((team) => (
                      <div
                        key={team.id}
                        className="bg-secondary px-3 py-1.5 rounded-lg text-[13px] cursor-pointer hover:bg-accent transition-colors"
                        onClick={() => navigate(`/teams/${team.id}`)}
                      >
                        <div>{team.name}</div>
                        <div className="text-[11px] text-muted-foreground">{team.lead}</div>
                      </div>
                    ))}
                  </div>
                </div>
              </Card>
            );
          })}
        </div>
      )}
    </div>
  );
}
