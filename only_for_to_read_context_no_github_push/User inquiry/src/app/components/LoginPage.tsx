import { useState } from "react";
import { useNavigate, Link } from "react-router";
import { Button, InputField, Card } from "./ui";

export function LoginPage() {
  const navigate = useNavigate();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!email || !password) {
      setError("Please enter both email and password.");
      return;
    }
    if (password === "wrong") {
      setError("Invalid email or password. Please try again.");
      return;
    }
    navigate("/");
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
            <h2>Log in</h2>
            {error && (
              <div className="bg-red-50 text-destructive text-[13px] px-3 py-2 rounded-lg border border-red-200">{error}</div>
            )}
            <InputField label="Email" type="email" placeholder="you@sky.uk" value={email} onChange={(e) => setEmail(e.target.value)} />
            <InputField label="Password" type="password" placeholder="Enter your password" value={password} onChange={(e) => setPassword(e.target.value)} />
            <div className="text-right">
              <Link to="/forgot-password" className="text-[13px] text-primary hover:underline">Forgot password?</Link>
            </div>
            <Button type="submit" className="w-full">Log in</Button>
            <p className="text-[13px] text-center text-muted-foreground">
              Don't have an account? <Link to="/signup" className="text-primary hover:underline">Sign up</Link>
            </p>
          </form>
        </Card>
      </div>
    </div>
  );
}
