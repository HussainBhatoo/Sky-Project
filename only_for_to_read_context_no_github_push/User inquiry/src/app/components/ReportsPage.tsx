import { Download, FileText } from "lucide-react";
import { Card, StatCard, Button } from "./ui";
import { teams, departments } from "../data";
import { toast } from "sonner";

export function ReportsPage() {
  const totalTeams = teams.length;
  const activeTeams = teams.filter((t) => t.status === "Active").length;
  const restructuring = teams.filter((t) => t.status === "Restructuring").length;
  const avgUpstream = (teams.reduce((s, t) => s + t.upstream.length, 0) / totalTeams).toFixed(1);
  const avgDownstream = (teams.reduce((s, t) => s + t.downstream.length, 0) / totalTeams).toFixed(1);

  const handleExport = (format: string) => {
    toast.success(`Report exported as ${format}`);
  };

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <h1>Reports</h1>
        <div className="flex gap-2">
          <Button variant="secondary" size="sm" onClick={() => handleExport("CSV")}>
            <Download size={14} /> Export CSV
          </Button>
          <Button variant="secondary" size="sm" onClick={() => handleExport("PDF")}>
            <Download size={14} /> Export PDF
          </Button>
        </div>
      </div>

      <div className="grid grid-cols-4 gap-4">
        <StatCard label="Total Teams" value={totalTeams} />
        <StatCard label="Active Teams" value={activeTeams} />
        <StatCard label="Restructuring" value={restructuring} />
        <StatCard label="Departments" value={departments.length} />
      </div>

      <div className="grid grid-cols-2 gap-4">
        <StatCard label="Avg. Upstream Dependencies" value={avgUpstream} />
        <StatCard label="Avg. Downstream Dependencies" value={avgDownstream} />
      </div>

      <Card>
        <h3 className="mb-3">Teams by Department</h3>
        <table className="w-full text-[14px]">
          <thead>
            <tr className="text-left text-muted-foreground border-b border-border">
              <th className="pb-2 font-[var(--font-weight-medium)]">Department</th>
              <th className="pb-2 font-[var(--font-weight-medium)]">Head(s)</th>
              <th className="pb-2 font-[var(--font-weight-medium)]">Teams</th>
            </tr>
          </thead>
          <tbody>
            {departments.map((d) => (
              <tr key={d.name} className="border-b border-border last:border-b-0">
                <td className="py-2">{d.name}</td>
                <td className="py-2 text-muted-foreground">{d.heads.join(", ")}</td>
                <td className="py-2">{d.teamIds.length}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </Card>

      <Card>
        <h3 className="mb-3">Teams with Most Dependencies</h3>
        <table className="w-full text-[14px]">
          <thead>
            <tr className="text-left text-muted-foreground border-b border-border">
              <th className="pb-2 font-[var(--font-weight-medium)]">Team</th>
              <th className="pb-2 font-[var(--font-weight-medium)]">Upstream</th>
              <th className="pb-2 font-[var(--font-weight-medium)]">Downstream</th>
              <th className="pb-2 font-[var(--font-weight-medium)]">Total</th>
            </tr>
          </thead>
          <tbody>
            {[...teams]
              .sort((a, b) => (b.upstream.length + b.downstream.length) - (a.upstream.length + a.downstream.length))
              .slice(0, 10)
              .map((t) => (
                <tr key={t.id} className="border-b border-border last:border-b-0">
                  <td className="py-2">{t.name}</td>
                  <td className="py-2">{t.upstream.length}</td>
                  <td className="py-2">{t.downstream.length}</td>
                  <td className="py-2">{t.upstream.length + t.downstream.length}</td>
                </tr>
              ))}
          </tbody>
        </table>
      </Card>
    </div>
  );
}
