import { useState } from "react";
import { useNavigate, Link } from "react-router";
import { Button, InputField, Card } from "./ui";

export function SignupPage() {
  const navigate = useNavigate();
  const [form, setForm] = useState({ name: "", email: "", password: "", confirm: "" });
  const [errors, setErrors] = useState<Record<string, string>>({});

  const validate = () => {
    const e: Record<string, string> = {};
    if (!form.name) e.name = "Full name is required.";
    if (!form.email) e.email = "Email is required.";
    else if (!form.email.includes("@")) e.email = "Please enter a valid email address.";
    if (!form.password) e.password = "Password is required.";
    else if (form.password.length < 8) e.password = "Password must be at least 8 characters.";
    if (form.password !== form.confirm) e.confirm = "Passwords do not match.";
    return e;
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    const errs = validate();
    setErrors(errs);
    if (Object.keys(errs).length === 0) {
      navigate("/login");
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-background p-4">
      <div className="w-full max-w-[400px]">
        <div className="text-center mb-8">
          <h1 className="mb-1">sky engineering</h1>
          <p className="text-muted-foreground text-[14px]">Team Registry Portal</p>
        </div>
        <Card>
          <form onSubmit={handleSubmit} className="space-y-4">
            <h2>Create account</h2>
            <InputField label="Full name" placeholder="John Doe" value={form.name} onChange={(e) => setForm({ ...form, name: e.target.value })} error={errors.name} />
            <InputField label="Email" type="email" placeholder="you@sky.uk" value={form.email} onChange={(e) => setForm({ ...form, email: e.target.value })} error={errors.email} />
            <InputField label="Password" type="password" placeholder="Min. 8 characters" value={form.password} onChange={(e) => setForm({ ...form, password: e.target.value })} error={errors.password} helper="At least 8 characters" />
            <InputField label="Confirm password" type="password" placeholder="Re-enter password" value={form.confirm} onChange={(e) => setForm({ ...form, confirm: e.target.value })} error={errors.confirm} />
            <Button type="submit" className="w-full">Sign up</Button>
            <p className="text-[13px] text-center text-muted-foreground">
              Already have an account? <Link to="/login" className="text-primary hover:underline">Log in</Link>
            </p>
          </form>
        </Card>
      </div>
    </div>
  );
}
