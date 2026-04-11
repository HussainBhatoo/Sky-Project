import React from "react";
import { NavLink, Outlet, useNavigate } from "react-router";
import {
  LayoutDashboard, Users, Building2, GitBranch, Mail, Calendar, FileText,
  ClipboardList, Settings, LogOut, User, Search, ChevronDown,
} from "lucide-react";
import { useState } from "react";

const navItems = [
  { to: "/", icon: LayoutDashboard, label: "Dashboard" },
  { to: "/teams", icon: Users, label: "Teams" },
  { to: "/departments", icon: Building2, label: "Departments" },
  { to: "/dependencies", icon: GitBranch, label: "Dependencies" },
  { to: "/messages", icon: Mail, label: "Messages" },
  { to: "/schedule", icon: Calendar, label: "Schedule" },
  { to: "/reports", icon: FileText, label: "Reports" },
  { to: "/audit", icon: ClipboardList, label: "Audit Log" },
  { to: "/admin", icon: Settings, label: "Admin" },
];

export function Layout() {
  const navigate = useNavigate();
  const [userMenuOpen, setUserMenuOpen] = useState(false);

  const handleLogout = () => {
    navigate("/login");
  };

  return (
    <div className="flex h-screen bg-background overflow-hidden">
      {/* Sidebar */}
      <aside className="w-[220px] shrink-0 bg-sidebar border-r border-sidebar-border flex flex-col">
        <div className="px-5 py-5 border-b border-sidebar-border">
          <span className="text-[18px] tracking-tight">sky engineering</span>
        </div>
        <nav className="flex-1 py-2 px-2 space-y-0.5 overflow-y-auto">
          {navItems.map((item) => (
            <NavLink
              key={item.to}
              to={item.to}
              end={item.to === "/"}
              className={({ isActive }) =>
                `flex items-center gap-3 px-3 py-2 rounded-lg text-[14px] transition-colors ${
                  isActive
                    ? "bg-sidebar-accent text-sidebar-accent-foreground"
                    : "text-sidebar-foreground/70 hover:bg-sidebar-accent/50 hover:text-sidebar-foreground"
                }`
              }
            >
              <item.icon size={18} />
              {item.label}
            </NavLink>
          ))}
        </nav>
      </aside>

      {/* Main area */}
      <div className="flex-1 flex flex-col min-w-0">
        {/* Header */}
        <header className="h-14 shrink-0 border-b border-border flex items-center justify-between px-6 bg-card">
          <div />
          <div className="relative">
            <button
              className="flex items-center gap-2 text-[14px] hover:bg-accent px-3 py-1.5 rounded-lg cursor-pointer"
              onClick={() => setUserMenuOpen(!userMenuOpen)}
            >
              <div className="w-7 h-7 rounded-full bg-primary text-primary-foreground flex items-center justify-center text-[12px]">JD</div>
              <span>John Doe</span>
              <ChevronDown size={14} />
            </button>
            {userMenuOpen && (
              <div className="absolute right-0 top-full mt-1 bg-card border border-border rounded-lg shadow-lg py-1 w-[160px] z-50">
                <button
                  className="flex items-center gap-2 px-3 py-2 text-[14px] w-full hover:bg-accent cursor-pointer"
                  onClick={() => { setUserMenuOpen(false); navigate("/profile"); }}
                >
                  <User size={16} /> Profile
                </button>
                <button
                  className="flex items-center gap-2 px-3 py-2 text-[14px] w-full hover:bg-accent cursor-pointer"
                  onClick={() => { setUserMenuOpen(false); handleLogout(); }}
                >
                  <LogOut size={16} /> Log out
                </button>
              </div>
            )}
          </div>
        </header>

        {/* Page content */}
        <main className="flex-1 overflow-y-auto p-6">
          <Outlet />
        </main>
      </div>
    </div>
  );
}
