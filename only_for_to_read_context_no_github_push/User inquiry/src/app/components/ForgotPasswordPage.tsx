import { useState } from "react";
import { Link } from "react-router";
import { Button, InputField, Card } from "./ui";

export function ForgotPasswordPage() {
  const [email, setEmail] = useState("");
  const [sent, setSent] = useState(false);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (email) setSent(true);
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-background p-4">
      <div className="w-full max-w-[400px]">
        <div className="text-center mb-8">
          <h1 className="mb-1">sky engineering</h1>
          <p className="text-muted-foreground text-[14px]">Team Registry Portal</p>
        </div>
        <Card>
          {sent ? (
            <div className="text-center space-y-3">
              <h2>Check your email</h2>
              <p className="text-[14px] text-muted-foreground">We've sent a password reset link to <strong>{email}</strong></p>
              <Link to="/login" className="text-[14px] text-primary hover:underline">Back to login</Link>
            </div>
          ) : (
            <form onSubmit={handleSubmit} className="space-y-4">
              <h2>Forgot password</h2>
              <p className="text-[14px] text-muted-foreground">Enter your email and we'll send you a reset link.</p>
              <InputField label="Email" type="email" placeholder="you@sky.uk" value={email} onChange={(e) => setEmail(e.target.value)} />
              <Button type="submit" className="w-full">Send reset link</Button>
              <p className="text-[13px] text-center">
                <Link to="/login" className="text-primary hover:underline">Back to login</Link>
              </p>
            </form>
          )}
        </Card>
      </div>
    </div>
  );
}
