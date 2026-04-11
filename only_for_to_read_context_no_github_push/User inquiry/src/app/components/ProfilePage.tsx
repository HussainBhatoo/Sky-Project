import { useState } from "react";
import { Button, InputField, Card } from "./ui";
import { toast } from "sonner";

export function ProfilePage() {
  const [profile, setProfile] = useState({ name: "John Doe", email: "john.doe@sky.uk", role: "Engineering Manager" });
  const [passwords, setPasswords] = useState({ current: "", newPass: "", confirm: "" });

  const handleSaveProfile = (e: React.FormEvent) => {
    e.preventDefault();
    toast.success("Profile saved");
  };

  const handleChangePassword = (e: React.FormEvent) => {
    e.preventDefault();
    if (passwords.newPass !== passwords.confirm) {
      toast.error("Passwords do not match");
      return;
    }
    toast.success("Password changed");
    setPasswords({ current: "", newPass: "", confirm: "" });
  };

  return (
    <div className="max-w-[600px] space-y-6">
      <h1>Profile</h1>

      <Card>
        <form onSubmit={handleSaveProfile} className="space-y-4">
          <h3>Edit profile</h3>
          <InputField label="Full name" value={profile.name} onChange={(e) => setProfile({ ...profile, name: e.target.value })} />
          <InputField label="Email" type="email" value={profile.email} onChange={(e) => setProfile({ ...profile, email: e.target.value })} />
          <InputField label="Role" value={profile.role} onChange={(e) => setProfile({ ...profile, role: e.target.value })} />
          <Button type="submit">Save changes</Button>
        </form>
      </Card>

      <Card>
        <form onSubmit={handleChangePassword} className="space-y-4">
          <h3>Change password</h3>
          <InputField label="Current password" type="password" value={passwords.current} onChange={(e) => setPasswords({ ...passwords, current: e.target.value })} />
          <InputField label="New password" type="password" value={passwords.newPass} onChange={(e) => setPasswords({ ...passwords, newPass: e.target.value })} helper="At least 8 characters" />
          <InputField label="Confirm new password" type="password" value={passwords.confirm} onChange={(e) => setPasswords({ ...passwords, confirm: e.target.value })} />
          <Button type="submit">Update password</Button>
        </form>
      </Card>
    </div>
  );
}
