import { useState, useEffect } from "react";
import { useParams, useNavigate } from "react-router";
import {
  ArrowLeft, Mail, Calendar, GitBranch, ExternalLink, Hash, Users,
  Clock, AlertTriangle,
} from "lucide-react";
import { Button, Card, Chip, StatusChip, EmptyState, Skeleton, Modal } from "./ui";
import { getTeamById, getTeamIdByName, teams, type Team } from "../data";
import { toast } from "sonner";

export function TeamDetailsPage() {
  const { teamId } = useParams();
  const navigate = useNavigate();
  const [loading, setLoading] = useState(true);
  const [team, setTeam] = useState<Team | undefined>();
  const [showDisbandModal, setShowDisbandModal] = useState(false);

  useEffect(() => {
    setLoading(true);
    const t = setTimeout(() => {
      setTeam(getTeamById(teamId || ""));
      setLoading(false);
    }, 500);
    return () => clearTimeout(t);
  }, [teamId]);

  if (loading) {
    return (
      <div className="space-y-4 max-w-[900px]">
        <Skeleton className="h-8 w-64" />
        <Skeleton className="h-5 w-48" />
        <div className="grid grid-cols-2 gap-4">
          <Skeleton className="h-32" />
          <Skeleton className="h-32" />
        </div>
        <Skeleton className="h-48" />
      </div>
    );
  }

  if (!team) {
    return (
      <div>
        <Button variant="ghost" onClick={() => navigate("/teams")}>
          <ArrowLeft size={16} /> Back to Teams
        </Button>
        <EmptyState title="Team not found" description="The team you're looking for doesn't exist." />
      </div>
    );
  }

  const handleEmailTeam = () => {
    navigate("/messages?compose=true&to=" + encodeURIComponent(team.name));
  };

  const handleScheduleMeeting = () => {
    navigate("/schedule?new=true&team=" + encodeURIComponent(team.name));
  };

  const handleViewDependencies = () => {
    navigate("/dependencies?focus=" + encodeURIComponent(team.name));
  };

  const dept = team.department;

  return (
    <div className="space-y-6 max-w-[900px]">
      <Button variant="ghost" onClick={() => navigate("/teams")} size="sm">
        <ArrowLeft size={16} /> Back to Teams
      </Button>

      {/* Header */}
      <div className="flex items-start justify-between">
        <div>
          <div className="flex items-center gap-3 mb-1">
            <h1>{team.name}</h1>
            <StatusChip status={team.status} />
          </div>
          <p className="text-[14px] text-muted-foreground">
            <Chip variant="department">{dept}</Chip>
            <span className="ml-3">Lead: <a href={`mailto:${team.leadEmail}`} className="text-primary hover:underline">{team.lead}</a></span>
          </p>
        </div>
        <div className="flex gap-2">
          <Button variant="secondary" size="sm" onClick={handleEmailTeam}><Mail size={16} /> Email team</Button>
          <Button variant="secondary" size="sm" onClick={handleScheduleMeeting}><Calendar size={16} /> Schedule meeting</Button>
          <Button variant="secondary" size="sm" onClick={handleViewDependencies}><GitBranch size={16} /> View dependencies</Button>
        </div>
      </div>

      {/* Mission */}
      <Card>
        <h4 className="mb-2">Mission / Responsibilities</h4>
        <p className="text-[14px] text-muted-foreground">{team.mission}</p>
      </Card>

      {/* Two columns: Contacts + Repos / Tech */}
      <div className="grid grid-cols-2 gap-4">
        <Card>
          <h4 className="mb-3">Contacts</h4>
          <div className="space-y-2 text-[14px]">
            <div className="flex items-center gap-2"><Hash size={14} className="text-muted-foreground" /> Slack: <span className="text-primary">{team.slackChannel}</span></div>
            <div className="flex items-center gap-2"><Mail size={14} className="text-muted-foreground" /> Email: <span className="text-primary">{team.email}</span></div>
          </div>
        </Card>
        <Card>
          <h4 className="mb-3">Links</h4>
          <div className="space-y-2 text-[14px]">
            <div className="flex items-center gap-2">
              <ExternalLink size={14} className="text-muted-foreground" />
              <a href={team.repoUrl} className="text-primary hover:underline" target="_blank" rel="noreferrer">GitHub Repository</a>
            </div>
            <div className="flex items-center gap-2">
              <ExternalLink size={14} className="text-muted-foreground" />
              <a href={team.jiraUrl} className="text-primary hover:underline" target="_blank" rel="noreferrer">Jira Board</a>
            </div>
          </div>
        </Card>
      </div>

      {/* Tech tags */}
      <Card>
        <h4 className="mb-3">Tech & Skills</h4>
        <div className="flex flex-wrap gap-2">
          {team.techTags.map((tag) => (
            <Chip key={tag}>{tag}</Chip>
          ))}
        </div>
      </Card>

      {/* Members */}
      <Card>
        <h4 className="mb-3"><Users size={16} className="inline mr-1" /> Team Members ({team.members.length})</h4>
        <table className="w-full text-[14px]">
          <thead>
            <tr className="text-left text-muted-foreground border-b border-border">
              <th className="pb-2 font-[var(--font-weight-medium)]">Name</th>
              <th className="pb-2 font-[var(--font-weight-medium)]">Role</th>
              <th className="pb-2 font-[var(--font-weight-medium)]">Email</th>
            </tr>
          </thead>
          <tbody>
            {team.members.map((m) => (
              <tr key={m.email} className="border-b border-border last:border-b-0">
                <td className="py-2">{m.name}</td>
                <td className="py-2 text-muted-foreground">{m.role}</td>
                <td className="py-2 text-primary">{m.email}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </Card>

      {/* Dependencies */}
      <div className="grid grid-cols-2 gap-4">
        <Card>
          <h4 className="mb-3">Upstream Dependencies</h4>
          {team.upstream.length === 0 ? (
            <EmptyState title="No upstream dependencies" description="This team has no upstream dependencies." />
          ) : (
            <div className="flex flex-wrap gap-2">
              {team.upstream.map((name) => (
                <Chip
                  key={name}
                  variant="upstream"
                  onClick={() => navigate(`/teams/${getTeamIdByName(name)}`)}
                >
                  {name}
                </Chip>
              ))}
            </div>
          )}
        </Card>
        <Card>
          <h4 className="mb-3">Downstream Dependencies</h4>
          {team.downstream.length === 0 ? (
            <EmptyState title="No downstream dependencies" description="This team has no downstream dependencies." />
          ) : (
            <div className="flex flex-wrap gap-2">
              {team.downstream.map((name) => (
                <Chip
                  key={name}
                  variant="downstream"
                  onClick={() => navigate(`/teams/${getTeamIdByName(name)}`)}
                >
                  {name}
                </Chip>
              ))}
            </div>
          )}
        </Card>
      </div>

      {/* Audit info */}
      <Card className="bg-muted/30">
        <div className="flex items-center justify-between text-[13px]">
          <span className="text-muted-foreground">
            <Clock size={14} className="inline mr-1" />
            Last updated by <strong>{team.lastUpdatedBy}</strong> on {team.lastUpdatedAt}
          </span>
          <button className="text-primary hover:underline cursor-pointer" onClick={() => navigate("/audit")}>View audit log</button>
        </div>
      </Card>

      {/* Lifecycle actions (UI-only) */}
      {team.status === "Active" && (
        <div className="flex gap-2">
          <Button variant="destructive" size="sm" onClick={() => setShowDisbandModal(true)}>
            <AlertTriangle size={14} /> Mark as Disbanded
          </Button>
        </div>
      )}

      <Modal
        open={showDisbandModal}
        onClose={() => setShowDisbandModal(false)}
        title="Confirm Status Change"
        actions={
          <>
            <Button variant="secondary" onClick={() => setShowDisbandModal(false)}>Cancel</Button>
            <Button variant="destructive" onClick={() => { setShowDisbandModal(false); toast.success("Team status updated to Disbanded"); }}>
              Confirm Disband
            </Button>
          </>
        }
      >
        <p className="text-[14px]">
          Are you sure you want to mark <strong>{team.name}</strong> as Disbanded? This action will be logged in the audit trail.
        </p>
      </Modal>
    </div>
  );
}
