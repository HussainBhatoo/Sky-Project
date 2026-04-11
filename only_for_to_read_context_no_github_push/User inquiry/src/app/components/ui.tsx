import React, { useState } from "react";
import { X } from "lucide-react";

// ---------- Button ----------
interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: "primary" | "secondary" | "destructive" | "ghost";
  size?: "sm" | "md";
}

export function Button({ variant = "primary", size = "md", className = "", children, ...props }: ButtonProps) {
  const base = "inline-flex items-center justify-center gap-2 rounded-lg transition-colors disabled:opacity-50 cursor-pointer";
  const sizes = size === "sm" ? "px-3 py-1.5 text-[13px]" : "px-4 py-2";
  const variants: Record<string, string> = {
    primary: "bg-primary text-primary-foreground hover:opacity-90",
    secondary: "bg-secondary text-secondary-foreground hover:bg-accent",
    destructive: "bg-destructive text-destructive-foreground hover:opacity-90",
    ghost: "hover:bg-accent text-foreground",
  };
  return (
    <button className={`${base} ${sizes} ${variants[variant]} ${className}`} {...props}>
      {children}
    </button>
  );
}

// ---------- Input ----------
interface InputFieldProps extends React.InputHTMLAttributes<HTMLInputElement> {
  label?: string;
  helper?: string;
  error?: string;
}

export function InputField({ label, helper, error, className = "", ...props }: InputFieldProps) {
  return (
    <div className={`flex flex-col gap-1 ${className}`}>
      {label && <label className="text-[14px]">{label}</label>}
      <input
        className={`px-3 py-2 rounded-lg border bg-input-background outline-none focus:ring-2 focus:ring-primary/30 ${error ? "border-destructive" : "border-border"}`}
        {...props}
      />
      {helper && !error && <span className="text-[12px] text-muted-foreground">{helper}</span>}
      {error && <span className="text-[12px] text-destructive">{error}</span>}
    </div>
  );
}

// ---------- Select ----------
interface SelectFieldProps {
  label?: string;
  value: string;
  onChange: (val: string) => void;
  options: { value: string; label: string }[];
  className?: string;
}

export function SelectField({ label, value, onChange, options, className = "" }: SelectFieldProps) {
  return (
    <div className={`flex flex-col gap-1 ${className}`}>
      {label && <label className="text-[14px]">{label}</label>}
      <select
        className="px-3 py-2 rounded-lg border border-border bg-input-background outline-none focus:ring-2 focus:ring-primary/30"
        value={value}
        onChange={(e) => onChange(e.target.value)}
      >
        {options.map((o) => (
          <option key={o.value} value={o.value}>{o.label}</option>
        ))}
      </select>
    </div>
  );
}

// ---------- Textarea ----------
interface TextareaFieldProps extends React.TextareaHTMLAttributes<HTMLTextAreaElement> {
  label?: string;
}

export function TextareaField({ label, className = "", ...props }: TextareaFieldProps) {
  return (
    <div className={`flex flex-col gap-1 ${className}`}>
      {label && <label className="text-[14px]">{label}</label>}
      <textarea
        className="px-3 py-2 rounded-lg border border-border bg-input-background outline-none focus:ring-2 focus:ring-primary/30 min-h-[80px] resize-y"
        {...props}
      />
    </div>
  );
}

// ---------- Card ----------
export function Card({ children, className = "", onClick }: { children: React.ReactNode; className?: string; onClick?: () => void }) {
  return (
    <div
      className={`bg-card border border-border rounded-xl p-4 shadow-sm ${onClick ? "cursor-pointer hover:shadow-md transition-shadow" : ""} ${className}`}
      onClick={onClick}
    >
      {children}
    </div>
  );
}

// ---------- Stat Card ----------
export function StatCard({ label, value, className = "" }: { label: string; value: string | number; className?: string }) {
  return (
    <Card className={className}>
      <div className="text-[13px] text-muted-foreground mb-1">{label}</div>
      <div className="text-[28px]">{value}</div>
    </Card>
  );
}

// ---------- Chip / Badge ----------
interface ChipProps {
  children: React.ReactNode;
  variant?: "default" | "active" | "restructuring" | "disbanded" | "department" | "upstream" | "downstream";
  onClick?: () => void;
  onRemove?: () => void;
}

export function Chip({ children, variant = "default", onClick, onRemove }: ChipProps) {
  const variantStyles: Record<string, string> = {
    default: "bg-secondary text-secondary-foreground",
    active: "bg-emerald-100 text-emerald-800",
    restructuring: "bg-amber-100 text-amber-800",
    disbanded: "bg-red-100 text-red-800",
    department: "bg-blue-100 text-blue-800",
    upstream: "bg-purple-100 text-purple-800",
    downstream: "bg-orange-100 text-orange-800",
  };
  return (
    <span
      className={`inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-[12px] ${variantStyles[variant]} ${onClick ? "cursor-pointer hover:opacity-80" : ""}`}
      onClick={onClick}
    >
      {children}
      {onRemove && (
        <button onClick={(e) => { e.stopPropagation(); onRemove(); }} className="hover:opacity-70 cursor-pointer">
          <X size={12} />
        </button>
      )}
    </span>
  );
}

export function StatusChip({ status }: { status: "Active" | "Restructuring" | "Disbanded" }) {
  const map = { Active: "active", Restructuring: "restructuring", Disbanded: "disbanded" } as const;
  return <Chip variant={map[status]}>{status}</Chip>;
}

// ---------- Tabs ----------
interface TabsProps {
  tabs: { key: string; label: string }[];
  active: string;
  onChange: (key: string) => void;
}

export function Tabs({ tabs, active, onChange }: TabsProps) {
  return (
    <div className="flex gap-0 border-b border-border">
      {tabs.map((t) => (
        <button
          key={t.key}
          className={`px-4 py-2 text-[14px] border-b-2 transition-colors cursor-pointer ${active === t.key ? "border-primary text-foreground" : "border-transparent text-muted-foreground hover:text-foreground"}`}
          onClick={() => onChange(t.key)}
        >
          {t.label}
        </button>
      ))}
    </div>
  );
}

// ---------- Modal ----------
interface ModalProps {
  open: boolean;
  onClose: () => void;
  title: string;
  children: React.ReactNode;
  actions?: React.ReactNode;
}

export function Modal({ open, onClose, title, children, actions }: ModalProps) {
  if (!open) return null;
  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/40" onClick={onClose}>
      <div className="bg-card rounded-xl shadow-xl p-6 max-w-[480px] w-full mx-4" onClick={(e) => e.stopPropagation()}>
        <div className="flex items-center justify-between mb-4">
          <h3>{title}</h3>
          <button onClick={onClose} className="text-muted-foreground hover:text-foreground cursor-pointer"><X size={20} /></button>
        </div>
        <div className="mb-4">{children}</div>
        {actions && <div className="flex justify-end gap-2">{actions}</div>}
      </div>
    </div>
  );
}

// ---------- Empty State ----------
export function EmptyState({ title, description, icon }: { title: string; description?: string; icon?: React.ReactNode }) {
  return (
    <div className="flex flex-col items-center justify-center py-12 text-center">
      {icon && <div className="text-muted-foreground mb-3">{icon}</div>}
      <div className="text-muted-foreground mb-1">{title}</div>
      {description && <div className="text-[13px] text-muted-foreground">{description}</div>}
    </div>
  );
}

// ---------- Skeleton ----------
export function Skeleton({ className = "" }: { className?: string }) {
  return <div className={`bg-muted animate-pulse rounded-lg ${className}`} />;
}

export function TableSkeleton({ rows = 5, cols = 4 }: { rows?: number; cols?: number }) {
  return (
    <div className="space-y-3">
      {Array.from({ length: rows }).map((_, i) => (
        <div key={i} className="flex gap-4">
          {Array.from({ length: cols }).map((_, j) => (
            <Skeleton key={j} className="h-8 flex-1" />
          ))}
        </div>
      ))}
    </div>
  );
}

// ---------- Toast (using sonner) ----------
// We'll use sonner's toast directly in components