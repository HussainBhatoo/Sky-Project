import { useState } from "react";
import { useNavigate } from "react-router";
import { Search, ArrowRight } from "lucide-react";
import { Card, StatCard } from "./ui";
import { teams, departments, auditLog, getTeamIdByName } from "../data";

export function DashboardPage() {
  const navigate = useNavigate();
  const [search, setSearch] = useState("");

  const totalTeams = teams.length;
  const totalDepts = departments.length;
  const noUpstream = teams.filter((t) => t.upstream.length === 0).length;
  const noDownstream = teams.filter((t) => t.downstream.length === 0).length;

  const searchResults = search.trim()
    ? teams.filter(
        (t) =>
          t.name.toLowerCase().includes(search.toLowerCase()) ||
          t.lead.toLowerCase().includes(search.toLowerCase()) ||
          t.department.toLowerCase().includes(search.toLowerCase())
      ).slice(0, 5)
    : [];

  return (
    <div className="space-y-6">
      <h1>Dashboard</h1>

      {/* Quick search */}
      <div className="relative max-w-[480px]">
        <Search size={18} className="absolute left-3 top-1/2 -translate-y-1/2 text-muted-foreground" />
        <input
          className="w-full pl-10 pr-4 py-2.5 rounded-lg border border-border bg-input-background outline-none focus:ring-2 focus:ring-primary/30"
          placeholder="Search teams, departments, or leads..."
          value={search}
          onChange={(e) => setSearch(e.target.value)}
        />
        {searchResults.length > 0 && (
          <div className="absolute top-full left-0 right-0 mt-1 bg-card border border-border rounded-lg shadow-lg z-10 py-1">
            {searchResults.map((t) => (
              <button
                key={t.id}
                className="w-full px-4 py-2 text-left hover:bg-accent flex items-center justify-between text-[14px] cursor-pointer"
                onClick={() => { setSearch(""); navigate(`/teams/${t.id}`); }}
              >
                <span>{t.name}</span>
                <span className="text-muted-foreground text-[12px]">{t.department}</span>
              </button>
            ))}
          </div>
        )}
      </div>

      {/* Stats */}
      <div className="grid grid-cols-4 gap-4">
        <StatCard label="Total Teams" value={totalTeams} />
        <StatCard label="Departments" value={totalDepts} />
        <StatCard label="No Upstream Dependencies" value={noUpstream} />
        <StatCard label="No Downstream Dependencies" value={noDownstream} />
      </div>

      {/* Recent updates */}
      <Card>
        <div className="flex items-center justify-between mb-3">
          <h3>Recent Updates</h3>
          <button className="text-[13px] text-primary hover:underline cursor-pointer" onClick={() => navigate("/audit")}>
            View all <ArrowRight size={14} className="inline" />
          </button>
        </div>
        <div className="space-y-0">
          {auditLog.slice(0, 5).map((entry) => (
            <div key={entry.id} className="flex items-center justify-between py-2.5 border-b border-border last:border-b-0">
              <div className="text-[14px]">
                <span>{entry.action} for </span>
                <button
                  className="text-primary hover:underline cursor-pointer"
                  onClick={() => navigate(`/teams/${getTeamIdByName(entry.target)}`)}
                >
                  {entry.target}
                </button>
                <span className="text-muted-foreground"> by {entry.user}</span>
              </div>
              <span className="text-[12px] text-muted-foreground shrink-0 ml-4">{entry.timestamp}</span>
            </div>
          ))}
        </div>
      </Card>
    </div>
  );
}
