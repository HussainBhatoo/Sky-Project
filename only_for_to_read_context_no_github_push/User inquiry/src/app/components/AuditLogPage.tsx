import { useState } from "react";
import { useNavigate } from "react-router";
import { Search } from "lucide-react";
import { Card } from "./ui";
import { auditLog, getTeamIdByName } from "../data";

export function AuditLogPage() {
  const navigate = useNavigate();
  const [search, setSearch] = useState("");

  const filtered = auditLog.filter(
    (e) =>
      !search ||
      e.action.toLowerCase().includes(search.toLowerCase()) ||
      e.target.toLowerCase().includes(search.toLowerCase()) ||
      e.user.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <div className="space-y-4">
      <h1>Audit Log</h1>
      <div className="relative max-w-[400px]">
        <Search size={18} className="absolute left-3 top-1/2 -translate-y-1/2 text-muted-foreground" />
        <input
          className="w-full pl-10 pr-4 py-2 rounded-lg border border-border bg-input-background outline-none focus:ring-2 focus:ring-primary/30 text-[14px]"
          placeholder="Search audit entries..."
          value={search}
          onChange={(e) => setSearch(e.target.value)}
        />
      </div>

      <Card>
        <table className="w-full text-[14px]">
          <thead>
            <tr className="text-left text-muted-foreground border-b border-border">
              <th className="pb-2 font-[var(--font-weight-medium)]">Action</th>
              <th className="pb-2 font-[var(--font-weight-medium)]">Team</th>
              <th className="pb-2 font-[var(--font-weight-medium)]">User</th>
              <th className="pb-2 font-[var(--font-weight-medium)]">Timestamp</th>
            </tr>
          </thead>
          <tbody>
            {filtered.map((entry) => (
              <tr key={entry.id} className="border-b border-border last:border-b-0">
                <td className="py-2.5">{entry.action}</td>
                <td className="py-2.5">
                  <button
                    className="text-primary hover:underline cursor-pointer"
                    onClick={() => navigate(`/teams/${getTeamIdByName(entry.target)}`)}
                  >
                    {entry.target}
                  </button>
                </td>
                <td className="py-2.5 text-muted-foreground">{entry.user}</td>
                <td className="py-2.5 text-muted-foreground">{entry.timestamp}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </Card>
    </div>
  );
}
