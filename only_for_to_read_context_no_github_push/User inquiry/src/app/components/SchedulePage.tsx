import { useState, useEffect } from "react";
import { useSearchParams } from "react-router";
import { Calendar, Clock, Plus } from "lucide-react";
import { Card, Button, InputField, TextareaField, SelectField } from "./ui";
import { scheduleEvents as mockEvents, teams, type ScheduleEvent } from "../data";
import { toast } from "sonner";

export function SchedulePage() {
  const [searchParams] = useSearchParams();
  const [events, setEvents] = useState(mockEvents);
  const [showForm, setShowForm] = useState(!!searchParams.get("new"));

  const prefillTeam = searchParams.get("team") || "";
  const [form, setForm] = useState({
    title: "",
    team: prefillTeam,
    date: "",
    time: "",
    description: "",
  });

  useEffect(() => {
    if (searchParams.get("new")) {
      setShowForm(true);
      setForm((f) => ({ ...f, team: searchParams.get("team") || "" }));
    }
  }, [searchParams]);

  const teamOptions = [
    { value: "", label: "Select a team" },
    ...teams.map((t) => ({ value: t.name, label: t.name })).sort((a, b) => a.label.localeCompare(b.label)),
  ];

  const handleSchedule = () => {
    if (!form.title || !form.team || !form.date || !form.time) return;
    const newEvent: ScheduleEvent = {
      id: String(events.length + 1),
      ...form,
    };
    setEvents([newEvent, ...events]);
    toast.success("Meeting scheduled");
    setShowForm(false);
    setForm({ title: "", team: "", date: "", time: "", description: "" });
  };

  // Simple calendar for current month
  const today = new Date(2026, 1, 26);
  const year = today.getFullYear();
  const month = today.getMonth();
  const daysInMonth = new Date(year, month + 1, 0).getDate();
  const firstDay = new Date(year, month, 1).getDay();
  const monthName = today.toLocaleString("default", { month: "long", year: "numeric" });

  return (
    <div className="space-y-4">
      <div className="flex items-center justify-between">
        <h1>Schedule</h1>
        <Button onClick={() => setShowForm(!showForm)} size="sm">
          <Plus size={16} /> Schedule Meeting
        </Button>
      </div>

      {showForm && (
        <Card className="max-w-[500px]">
          <h3 className="mb-4">New Meeting</h3>
          <div className="space-y-3">
            <InputField label="Title" placeholder="Meeting title" value={form.title} onChange={(e) => setForm({ ...form, title: e.target.value })} />
            <SelectField label="Team" value={form.team} onChange={(v) => setForm({ ...form, team: v })} options={teamOptions} />
            <div className="grid grid-cols-2 gap-3">
              <InputField label="Date" type="date" value={form.date} onChange={(e) => setForm({ ...form, date: e.target.value })} />
              <InputField label="Time" type="time" value={form.time} onChange={(e) => setForm({ ...form, time: e.target.value })} />
            </div>
            <TextareaField label="Description" placeholder="Optional notes" value={form.description} onChange={(e) => setForm({ ...form, description: e.target.value })} />
            <div className="flex gap-2">
              <Button onClick={handleSchedule}>Schedule</Button>
              <Button variant="secondary" onClick={() => setShowForm(false)}>Cancel</Button>
            </div>
          </div>
        </Card>
      )}

      <div className="grid grid-cols-3 gap-6">
        {/* Upcoming */}
        <div className="col-span-2">
          <h3 className="mb-3">Upcoming Meetings</h3>
          <div className="space-y-3">
            {events.map((ev) => (
              <Card key={ev.id}>
                <div className="flex items-start justify-between">
                  <div>
                    <h4>{ev.title}</h4>
                    <p className="text-[13px] text-muted-foreground">{ev.team}</p>
                    {ev.description && <p className="text-[13px] text-muted-foreground mt-1">{ev.description}</p>}
                  </div>
                  <div className="text-right text-[13px] text-muted-foreground shrink-0">
                    <div className="flex items-center gap-1"><Calendar size={12} /> {ev.date}</div>
                    <div className="flex items-center gap-1"><Clock size={12} /> {ev.time}</div>
                  </div>
                </div>
              </Card>
            ))}
          </div>
        </div>

        {/* Mini calendar */}
        <div>
          <h3 className="mb-3">Calendar</h3>
          <Card>
            <div className="text-center text-[14px] mb-3">{monthName}</div>
            <div className="grid grid-cols-7 gap-1 text-center text-[12px]">
              {["Su", "Mo", "Tu", "We", "Th", "Fr", "Sa"].map((d) => (
                <div key={d} className="text-muted-foreground py-1">{d}</div>
              ))}
              {Array.from({ length: firstDay }).map((_, i) => (
                <div key={"e" + i} />
              ))}
              {Array.from({ length: daysInMonth }).map((_, i) => {
                const day = i + 1;
                const isToday = day === today.getDate();
                const hasEvent = events.some((e) => {
                  const d = new Date(e.date);
                  return d.getDate() === day && d.getMonth() === month;
                });
                return (
                  <div
                    key={day}
                    className={`py-1 rounded ${isToday ? "bg-primary text-primary-foreground" : ""} ${hasEvent && !isToday ? "bg-blue-100" : ""}`}
                  >
                    {day}
                  </div>
                );
              })}
            </div>
          </Card>
        </div>
      </div>
    </div>
  );
}
