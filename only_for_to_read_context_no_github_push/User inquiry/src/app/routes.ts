import { createBrowserRouter } from "react-router";
import { Layout } from "./components/Layout";
import { LoginPage } from "./components/LoginPage";
import { SignupPage } from "./components/SignupPage";
import { ForgotPasswordPage } from "./components/ForgotPasswordPage";
import { ProfilePage } from "./components/ProfilePage";
import { DashboardPage } from "./components/DashboardPage";
import { TeamsListPage } from "./components/TeamsListPage";
import { TeamDetailsPage } from "./components/TeamDetailsPage";
import { DepartmentsPage } from "./components/DepartmentsPage";
import { DependenciesPage } from "./components/DependenciesPage";
import { MessagesPage } from "./components/MessagesPage";
import { SchedulePage } from "./components/SchedulePage";
import { ReportsPage } from "./components/ReportsPage";
import { AuditLogPage } from "./components/AuditLogPage";
import { AdminPage } from "./components/AdminPage";

export const router = createBrowserRouter([
  {
    path: "/login",
    Component: LoginPage,
  },
  {
    path: "/signup",
    Component: SignupPage,
  },
  {
    path: "/forgot-password",
    Component: ForgotPasswordPage,
  },
  {
    path: "/",
    Component: Layout,
    children: [
      { index: true, Component: DashboardPage },
      { path: "profile", Component: ProfilePage },
      { path: "teams", Component: TeamsListPage },
      { path: "teams/:teamId", Component: TeamDetailsPage },
      { path: "departments", Component: DepartmentsPage },
      { path: "dependencies", Component: DependenciesPage },
      { path: "messages", Component: MessagesPage },
      { path: "schedule", Component: SchedulePage },
      { path: "reports", Component: ReportsPage },
      { path: "audit", Component: AuditLogPage },
      { path: "admin", Component: AdminPage },
    ],
  },
]);
