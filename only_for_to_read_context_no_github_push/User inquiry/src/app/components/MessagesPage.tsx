import { useState, useEffect } from "react";
import { useSearchParams } from "react-router";
import { Mail, Send, Inbox, ArrowLeft } from "lucide-react";
import { Card, Button, InputField, TextareaField, Tabs, EmptyState, Chip } from "./ui";
import { messages as mockMessages, teams, type Message } from "../data";
import { toast } from "sonner";

export function MessagesPage() {
  const [searchParams] = useSearchParams();
  const [tab, setTab] = useState(searchParams.get("compose") ? "compose" : "inbox");
  const [msgs, setMsgs] = useState(mockMessages);
  const [selectedMsg, setSelectedMsg] = useState<Message | null>(null);

  // Compose state
  const prefillTo = searchParams.get("to") || "";
  const [composeTo, setComposeTo] = useState(prefillTo);
  const [composeSubject, setComposeSubject] = useState("");
  const [composeBody, setComposeBody] = useState("");

  useEffect(() => {
    if (searchParams.get("compose")) {
      setTab("compose");
      setComposeTo(searchParams.get("to") || "");
    }
  }, [searchParams]);

  const handleSend = () => {
    if (!composeTo || !composeSubject) return;
    toast.success("Message sent");
    setComposeTo("");
    setComposeSubject("");
    setComposeBody("");
    setTab("inbox");
  };

  return (
    <div className="space-y-4">
      <h1>Messages</h1>
      <Tabs
        tabs={[
          { key: "inbox", label: "Inbox" },
          { key: "compose", label: "Compose" },
        ]}
        active={tab}
        onChange={setTab}
      />

      {tab === "inbox" && !selectedMsg && (
        <div className="mt-4">
          {msgs.length === 0 ? (
            <EmptyState title="No messages" description="Your inbox is empty." icon={<Inbox size={40} />} />
          ) : (
            <Card>
              {msgs.map((msg) => (
                <div
                  key={msg.id}
                  className={`flex items-center justify-between py-3 px-2 border-b border-border last:border-b-0 cursor-pointer hover:bg-accent/50 rounded ${!msg.read ? "bg-blue-50/50" : ""}`}
                  onClick={() => { setSelectedMsg(msg); msg.read = true; }}
                >
                  <div className="flex items-center gap-3 min-w-0">
                    {!msg.read && <div className="w-2 h-2 rounded-full bg-primary shrink-0" />}
                    <div className="min-w-0">
                      <div className="text-[14px] truncate">{msg.subject}</div>
                      <div className="text-[12px] text-muted-foreground">From: {msg.from}</div>
                    </div>
                  </div>
                  <span className="text-[12px] text-muted-foreground shrink-0 ml-4">{msg.timestamp}</span>
                </div>
              ))}
            </Card>
          )}
        </div>
      )}

      {tab === "inbox" && selectedMsg && (
        <div className="mt-4">
          <Button variant="ghost" size="sm" onClick={() => setSelectedMsg(null)} className="mb-3">
            <ArrowLeft size={16} /> Back to inbox
          </Button>
          <Card>
            <h3 className="mb-2">{selectedMsg.subject}</h3>
            <div className="text-[13px] text-muted-foreground mb-4">
              From: {selectedMsg.from} · {selectedMsg.timestamp}
            </div>
            <p className="text-[14px]">{selectedMsg.body}</p>
          </Card>
        </div>
      )}

      {tab === "compose" && (
        <Card className="mt-4 max-w-[600px]">
          <h3 className="mb-4">New Message</h3>
          <div className="space-y-4">
            <InputField label="To" placeholder="Team or person name" value={composeTo} onChange={(e) => setComposeTo(e.target.value)} />
            <InputField label="Subject" placeholder="Enter subject" value={composeSubject} onChange={(e) => setComposeSubject(e.target.value)} />
            <TextareaField label="Message" placeholder="Type your message..." value={composeBody} onChange={(e) => setComposeBody(e.target.value)} />
            <Button onClick={handleSend}><Send size={16} /> Send message</Button>
          </div>
        </Card>
      )}
    </div>
  );
}
