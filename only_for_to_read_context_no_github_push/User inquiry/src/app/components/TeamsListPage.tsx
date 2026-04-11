import { useState, useEffect } from "react";
import { useNavigate } from "react-router";
import { Search, Filter, X, Inbox } from "lucide-react";
import { Card, Chip, StatusChip, EmptyState, Skeleton } from "./ui";
import { teams, departments, type Team } from "../data";

export function TeamsListPage() {
  const navigate = useNavigate();
  const [search, setSearch] = useState("");
  const [deptFilter, setDeptFilter] = useState("");
  const [statusFilter, setStatusFilter] = useState("");
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const t = setTimeout(() => setLoading(false), 800);
    return () => clearTimeout(t);
  }, []);

  const filtered = teams.filter((t) => {
    const matchSearch =
      !search ||
      t.name.toLowerCase().includes(search.toLowerCase()) ||
      t.name.replace("The ", "").toLowerCase().includes(search.toLowerCase()) ||
      ("the " + t.name).toLowerCase().includes(search.toLowerCase()) ||
      t.lead.toLowerCase().includes(search.toLowerCase()) ||
      t.department.toLowerCase().includes(search.toLowerCase());
    const matchDept = !deptFilter || t.department === deptFilter;
    const matchStatus = !statusFilter || t.status === statusFilter;
    return matchSearch && matchDept && matchStatus;
  });

  const hasFilters = !!deptFilter || !!statusFilter;

  return (
    <div className="space-y-4">
      <h1>Teams</h1>

      {/* Search + Filters */}
      <div className="flex items-center gap-3">
        <div className="relative flex-1 max-w-[400px]">
          <Search size={18} className="absolute left-3 top-1/2 -translate-y-1/2 text-muted-foreground" />
          <input
            className="w-full pl-10 pr-4 py-2 rounded-lg border border-border bg-input-background outline-none focus:ring-2 focus:ring-primary/30 text-[14px]"
            placeholder="Search by team, lead, or department..."
            value={search}
            onChange={(e) => setSearch(e.target.value)}
          />
        </div>
        <select
          className="px-3 py-2 rounded-lg border border-border bg-input-background text-[14px] outline-none"
          value={deptFilter}
          onChange={(e) => setDeptFilter(e.target.value)}
        >
          <option value="">All Departments</option>
          {departments.map((d) => (
            <option key={d.name} value={d.name}>{d.name}</option>
          ))}
        </select>
        <select
          className="px-3 py-2 rounded-lg border border-border bg-input-background text-[14px] outline-none"
          value={statusFilter}
          onChange={(e) => setStatusFilter(e.target.value)}
        >
          <option value="">All Statuses</option>
          <option value="Active">Active</option>
          <option value="Restructuring">Restructuring</option>
          <option value="Disbanded">Disbanded</option>
        </select>
      </div>

      {/* Active filter chips */}
      {hasFilters && (
        <div className="flex items-center gap-2">
          <span className="text-[13px] text-muted-foreground">Filters:</span>
          {deptFilter && <Chip variant="department" onRemove={() => setDeptFilter("")}>{deptFilter}</Chip>}
          {statusFilter && (
            <Chip
              variant={statusFilter === "Active" ? "active" : statusFilter === "Restructuring" ? "restructuring" : "disbanded"}
              onRemove={() => setStatusFilter("")}
            >
              {statusFilter}
            </Chip>
          )}
        </div>
      )}

      {/* Results count */}
      <p className="text-[13px] text-muted-foreground">{filtered.length} team{filtered.length !== 1 ? "s" : ""} found</p>

      {/* Loading state */}
      {loading ? (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {Array.from({ length: 6 }).map((_, i) => (
            <div key={i} className="border border-border rounded-xl p-4 space-y-3">
              <Skeleton className="h-5 w-3/4" />
              <Skeleton className="h-4 w-1/2" />
              <Skeleton className="h-4 w-full" />
              <div className="flex gap-2">
                <Skeleton className="h-5 w-16" />
                <Skeleton className="h-5 w-16" />
              </div>
            </div>
          ))}
        </div>
      ) : filtered.length === 0 ? (
        <EmptyState
          title="No teams found"
          description="Try adjusting your search or filters."
          icon={<Inbox size={40} />}
        />
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {filtered.map((team) => (
            <Card key={team.id} onClick={() => navigate(`/teams/${team.id}`)} className="hover:border-primary/30">
              <div className="flex items-start justify-between mb-2">
                <h4 className="pr-2">{team.name}</h4>
                <StatusChip status={team.status} />
              </div>
              <p className="text-[13px] text-muted-foreground mb-1">Lead: {team.lead}</p>
              <Chip variant="department">{team.department}</Chip>
              <p className="text-[13px] text-muted-foreground mt-2 line-clamp-2">{team.mission}</p>
              <div className="flex gap-3 mt-3 text-[12px] text-muted-foreground">
                <span>{team.upstream.length} upstream</span>
                <span>{team.downstream.length} downstream</span>
              </div>
            </Card>
          ))}
        </div>
      )}
    </div>
  );
}
