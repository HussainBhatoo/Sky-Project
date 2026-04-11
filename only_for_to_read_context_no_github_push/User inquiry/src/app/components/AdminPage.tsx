import { Users, Shield, Database, Settings } from "lucide-react";
import { Card } from "./ui";

export function AdminPage() {
  const adminItems = [
    { icon: Users, label: "User Management", description: "Add, edit, or remove user accounts and permissions." },
    { icon: Shield, label: "Roles & Permissions", description: "Configure access levels and role assignments." },
    { icon: Database, label: "Data Management", description: "Import/export team data, manage bulk operations." },
    { icon: Settings, label: "System Settings", description: "Configure portal settings and integrations." },
  ];

  return (
    <div className="space-y-4">
      <h1>Admin Hub</h1>
      <p className="text-[14px] text-muted-foreground">Administration tools for managing the Team Registry Portal.</p>

      <div className="grid grid-cols-2 gap-4 max-w-[700px]">
        {adminItems.map((item) => (
          <Card key={item.label} className="cursor-pointer hover:border-primary/30">
            <div className="flex items-start gap-3">
              <div className="p-2 bg-secondary rounded-lg">
                <item.icon size={20} />
              </div>
              <div>
                <h4>{item.label}</h4>
                <p className="text-[13px] text-muted-foreground mt-1">{item.description}</p>
              </div>
            </div>
          </Card>
        ))}
      </div>
    </div>
  );
}
