// Sky Engineering Team Registry - Mock Data

export interface TeamMember {
  name: string;
  role: string;
  email: string;
}

export interface Team {
  id: string;
  name: string;
  department: string;
  lead: string;
  leadEmail: string;
  status: "Active" | "Restructuring" | "Disbanded";
  upstream: string[];
  downstream: string[];
  members: TeamMember[];
  mission: string;
  slackChannel: string;
  email: string;
  repoUrl: string;
  jiraUrl: string;
  techTags: string[];
  lastUpdatedBy: string;
  lastUpdatedAt: string;
}

export interface Department {
  name: string;
  heads: string[];
  teamIds: string[];
}

export const departments: Department[] = [
  {
    name: "Arch",
    heads: ["Theodore Knox"],
    teamIds: ["the-dev-dragons", "the-microservice-mavericks"],
  },
  {
    name: "Mobile",
    heads: ["Adam Sinclair", "Violet Ramsey"],
    teamIds: [
      "the-api-explorers", "the-git-masters", "cache-me-outside", "devnull-pioneers",
      "infinite-loopers", "kernel-crushers", "the-404-not-found", "the-bit-manipulators",
      "the-code-refactors", "the-feature-crafters", "the-jenkins-juggernauts",
      "the-scrum-lords", "the-version-controllers",
    ],
  },
  {
    name: "Native TVs",
    heads: ["Mason Briggs"],
    teamIds: [
      "bug-exterminators", "code-monkeys", "data-wranglers", "exception-catchers",
      "git-good", "the-agile-alchemists", "the-ci-cd-squad", "the-compile-crew",
      "the-hotfix-heroes", "the-sprint-kings",
    ],
  },
  {
    name: "Programme",
    heads: ["Bella Monroe"],
    teamIds: ["the-quantum-coders"],
  },
  {
    name: "Reliability_Tool",
    heads: ["Lucy Vaughn"],
    teamIds: [
      "the-encryption-squad", "the-frontend-phantoms", "the-hackathon-hustlers",
      "the-lambda-legends", "the-ux-wizards",
    ],
  },
  {
    name: "xTV_Web",
    heads: ["Nora Chandler", "Sebastian Holt"],
    teamIds: [
      "api-avengers", "stack-overflow-survivors", "the-algorithm-alliance",
      "the-binary-beasts", "the-error-handlers", "agile-avengers", "bit-masters",
      "byte-force", "code-warriors", "devops-dynasty", "full-stack-ninjas",
      "syntax-squad", "the-cloud-architects", "the-codebreakers", "the-debuggers",
    ],
  },
];

function makeId(name: string): string {
  return name.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/(^-|-$)/g, "");
}

function makeSlack(name: string): string {
  return "#team-" + name.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/(^-|-$)/g, "");
}

function makeEmail(name: string): string {
  return name.toLowerCase().replace(/[^a-z0-9]+/g, "-") + "@sky.uk";
}

function makeMembers(lead: string, theme: string): TeamMember[] {
  const memberSets: Record<string, TeamMember[]> = {};
  // Generate deterministic members based on team name
  const firstNames = ["Alex", "Jordan", "Sam", "Taylor", "Morgan", "Casey", "Quinn", "Drew", "Avery", "Blake"];
  const lastNames = ["Walker", "Harris", "Young", "King", "Wright", "Green", "Adams", "Nelson", "Hill", "Moore"];
  const roles = ["Senior Engineer", "Engineer", "Junior Engineer", "QA Engineer", "DevOps Engineer"];

  const members: TeamMember[] = [
    { name: lead, role: "Team Lead", email: lead.toLowerCase().replace(" ", ".") + "@sky.uk" },
  ];
  const hash = theme.split("").reduce((a, c) => a + c.charCodeAt(0), 0);
  for (let i = 0; i < 5; i++) {
    const fi = (hash + i * 3) % firstNames.length;
    const li = (hash + i * 7) % lastNames.length;
    const ri = (hash + i) % roles.length;
    const name = firstNames[fi] + " " + lastNames[li];
    members.push({
      name,
      role: roles[ri],
      email: name.toLowerCase().replace(" ", ".") + "@sky.uk",
    });
  }
  return members;
}

const teamDataRaw: Array<{
  name: string; department: string; lead: string; upstream: string[]; downstream: string[];
  status?: "Active" | "Restructuring" | "Disbanded"; mission: string; techTags: string[];
}> = [
  // Arch
  { name: "The Dev Dragons", department: "Arch", lead: "Levi Bishop", upstream: ["API Avengers"], downstream: ["The Feature Crafters"], mission: "Designing and evolving core architectural patterns across Sky's engineering platform. Focused on system design reviews and technical standards.", techTags: ["System Design", "Architecture", "Java", "Kafka"] },
  { name: "The Microservice Mavericks", department: "Arch", lead: "Eleanor Freeman", upstream: [], downstream: ["The Lambda Legends", "The Code Refactors"], mission: "Building and maintaining microservice frameworks and shared libraries used across the organisation.", techTags: ["Microservices", "Spring Boot", "Docker", "gRPC"] },
  // Mobile
  { name: "The API Explorers", department: "Mobile", lead: "Julian Bell", upstream: ["DevNull Pioneers", "Full Stack Ninjas", "The Encryption Squad", "The Frontend Phantoms"], downstream: ["Full Stack Ninjas"], mission: "Integrating and testing mobile APIs for Sky's consumer applications on iOS and Android.", techTags: ["REST APIs", "Swift", "Kotlin", "Postman"] },
  { name: "The Git Masters", department: "Mobile", lead: "Victoria Price", upstream: [], downstream: ["The Version Controllers"], mission: "Managing version control workflows and branching strategies for the mobile division.", techTags: ["Git", "GitHub Actions", "CI/CD", "Branching"] },
  { name: "Cache Me Outside", department: "Mobile", lead: "Owen Barnes", upstream: ["The Cloud Architects"], downstream: ["The UX Wizards"], mission: "Optimising caching strategies and performance for mobile content delivery.", techTags: ["Redis", "CDN", "Caching", "Performance"] },
  { name: "DevNull Pioneers", department: "Mobile", lead: "Caleb Bryant", upstream: [], downstream: ["The API Explorers"], mission: "Exploring and prototyping experimental mobile features and developer tools.", techTags: ["Prototyping", "React Native", "Flutter", "R&D"] },
  { name: "Infinite Loopers", department: "Mobile", lead: "Madison Clarke", upstream: [], downstream: ["The Feature Crafters"], mission: "Handling iterative feature development cycles for mobile user experience.", techTags: ["Agile", "React Native", "TypeScript", "UX"] },
  { name: "Kernel Crushers", department: "Mobile", lead: "Leo Watson", upstream: ["The Quantum Coders"], downstream: ["API Avengers"], mission: "Low-level mobile performance optimisation and native module development.", techTags: ["C++", "NDK", "Performance", "Native Modules"] },
  { name: "The 404 Not Found", department: "Mobile", lead: "Nathan Fisher", upstream: ["The Version Controllers"], downstream: ["The Scrum Lords"], mission: "Error tracking, monitoring, and incident response for mobile applications.", techTags: ["Sentry", "Monitoring", "Incident Response", "Observability"] },
  { name: "The Bit Manipulators", department: "Mobile", lead: "Riley Sanders", upstream: ["Data Wranglers", "The Compile Crew"], downstream: ["The Binary Beasts"], mission: "Data encoding, compression, and binary format processing for streaming.", techTags: ["Data Processing", "Compression", "Python", "Streaming"] },
  { name: "The Code Refactors", department: "Mobile", lead: "Hannah Simmons", upstream: ["The Microservice Mavericks"], downstream: ["Bug Exterminators"], mission: "Continuous improvement of mobile codebase quality through refactoring and tech debt reduction.", techTags: ["Refactoring", "Code Quality", "Kotlin", "Swift"] },
  { name: "The Feature Crafters", department: "Mobile", lead: "Gabriel Coleman", upstream: ["Infinite Loopers", "Syntax Squad", "The Dev Dragons", "The UX Wizards"], downstream: ["Syntax Squad", "The Error Handlers"], mission: "Building new user-facing features for Sky's mobile apps, from design to delivery.", techTags: ["Feature Development", "React Native", "UI/UX", "A/B Testing"] },
  { name: "The Jenkins Juggernauts", department: "Mobile", lead: "Isaac Jenkins", upstream: [], downstream: ["DevOps Dynasty", "Git Good"], mission: "Maintaining and improving CI/CD pipelines using Jenkins for mobile builds.", techTags: ["Jenkins", "CI/CD", "Groovy", "Pipeline"] },
  { name: "The Scrum Lords", department: "Mobile", lead: "Chloe Hall", upstream: ["Stack Overflow Survivors", "The 404 Not Found"], downstream: ["Agile Avengers", "The Sprint Kings"], mission: "Facilitating agile delivery and sprint planning across mobile teams.", techTags: ["Scrum", "Jira", "Agile", "Project Management"] },
  { name: "The Version Controllers", department: "Mobile", lead: "Zoey Stevens", upstream: ["Code Monkeys", "Git Good", "The Git Masters"], downstream: ["The 404 Not Found", "The Compile Crew"], mission: "Ensuring stable release management and version control practices.", techTags: ["Git", "Release Management", "Versioning", "Automation"] },
  // Native TVs
  { name: "Bug Exterminators", department: "Native TVs", lead: "Lily Phillips", upstream: ["The Code Refactors"], downstream: ["The Debuggers"], mission: "Identifying, triaging, and resolving bugs across Sky's TV platform applications.", techTags: ["Bug Tracking", "QA", "Selenium", "Test Automation"] },
  { name: "Code Monkeys", department: "Native TVs", lead: "Harper Lewis", upstream: ["The Hotfix Heroes"], downstream: ["The Version Controllers"], mission: "Rapid development and feature implementation for native TV applications.", techTags: ["C++", "TV SDK", "Embedded", "Linux"] },
  { name: "Data Wranglers", department: "Native TVs", lead: "Alexander Perry", upstream: [], downstream: ["The Bit Manipulators"], mission: "Managing data pipelines and ETL processes for TV platform analytics.", techTags: ["ETL", "Python", "SQL", "Data Pipelines"] },
  { name: "Exception Catchers", department: "Native TVs", lead: "Daniel Scott", upstream: [], downstream: ["The Debuggers"], mission: "Error handling frameworks and crash reporting for TV applications.", techTags: ["Crash Reporting", "Logging", "Splunk", "Error Handling"] },
  { name: "Git Good", department: "Native TVs", lead: "Scarlett Edwards", upstream: ["The Jenkins Juggernauts"], downstream: ["The Version Controllers"], mission: "Promoting Git best practices and workflow automation for the TV division.", techTags: ["Git", "Automation", "Shell Scripts", "GitHub"] },
  { name: "The Agile Alchemists", department: "Native TVs", lead: "Samuel Morgan", upstream: ["The Sprint Kings"], downstream: ["Stack Overflow Survivors"], mission: "Transforming agile processes and continuous improvement for Native TV teams.", techTags: ["Agile", "Kanban", "Retrospectives", "Coaching"] },
  { name: "The CI/CD Squad", department: "Native TVs", lead: "Jack Turner", upstream: ["The Hotfix Heroes"], downstream: ["Syntax Squad"], mission: "Building and maintaining continuous integration and deployment infrastructure.", techTags: ["CI/CD", "Jenkins", "Docker", "Kubernetes"] },
  { name: "The Compile Crew", department: "Native TVs", lead: "Matthew Reed", upstream: ["The Version Controllers"], downstream: ["The Bit Manipulators"], mission: "Managing build systems and compilation pipelines for TV platform software.", techTags: ["Build Systems", "CMake", "Gradle", "Compilation"] },
  { name: "The Hotfix Heroes", department: "Native TVs", lead: "Grace Patterson", upstream: [], downstream: ["Code Monkeys", "The CI/CD Squad"], mission: "Rapid response team for critical production fixes on TV platforms.", techTags: ["Hotfixes", "On-Call", "Production Support", "Incident Response"] },
  { name: "The Sprint Kings", department: "Native TVs", lead: "Evelyn Hughes", upstream: ["Agile Avengers", "The Scrum Lords"], downstream: ["The Agile Alchemists"], mission: "Driving sprint execution and delivery excellence across TV engineering.", techTags: ["Sprint Planning", "Jira", "Delivery", "Metrics"] },
  // Programme
  { name: "The Quantum Coders", department: "Programme", lead: "Hudson Ford", upstream: [], downstream: ["Kernel Crushers"], mission: "Researching and prototyping next-generation computing approaches for Sky's infrastructure.", techTags: ["Research", "Quantum Computing", "Python", "Innovation"] },
  // Reliability_Tool
  { name: "The Encryption Squad", department: "Reliability_Tool", lead: "Ethan Griffin", upstream: ["The Codebreakers"], downstream: ["API Avengers", "The API Explorers"], mission: "Implementing and maintaining encryption standards and security protocols.", techTags: ["Encryption", "Security", "TLS", "PKI"] },
  { name: "The Frontend Phantoms", department: "Reliability_Tool", lead: "Stella Martinez", upstream: [], downstream: ["The API Explorers"], mission: "Building reliability tooling dashboards and frontend monitoring interfaces.", techTags: ["React", "TypeScript", "Dashboards", "Monitoring UI"] },
  { name: "The Hackathon Hustlers", department: "Reliability_Tool", lead: "Dylan Spencer", upstream: [], downstream: ["The UX Wizards"], mission: "Running innovation sprints and hackathons to improve reliability tooling.", techTags: ["Innovation", "Hackathons", "Prototyping", "Tooling"] },
  { name: "The Lambda Legends", department: "Reliability_Tool", lead: "Layla Russell", upstream: ["The Microservice Mavericks"], downstream: ["API Avengers"], mission: "Developing serverless functions and event-driven reliability tools.", techTags: ["AWS Lambda", "Serverless", "Node.js", "Event-Driven"] },
  { name: "The UX Wizards", department: "Reliability_Tool", lead: "Aurora Cooper", upstream: ["Cache Me Outside", "The Hackathon Hustlers"], downstream: ["The Feature Crafters", "Full Stack Ninjas"], mission: "Designing user experiences for internal reliability and engineering tools.", techTags: ["UX Design", "Figma", "User Research", "Accessibility"] },
  // xTV_Web
  { name: "API Avengers", department: "xTV_Web", lead: "Henry Ward", upstream: ["Bit Masters", "Byte Force", "Kernel Crushers", "The Encryption Squad", "The Lambda Legends"], downstream: ["The Dev Dragons"], mission: "Building and scaling the core API gateway for Sky's xTV web platform.", techTags: ["API Gateway", "Node.js", "GraphQL", "Scalability"] },
  { name: "Stack Overflow Survivors", department: "xTV_Web", lead: "Lucas Foster", upstream: ["The Agile Alchemists"], downstream: ["The Scrum Lords"], mission: "Knowledge sharing and developer support across xTV web engineering teams.", techTags: ["Documentation", "Knowledge Base", "Mentoring", "Confluence"] },
  { name: "The Algorithm Alliance", department: "xTV_Web", lead: "Amelia Brooks", upstream: ["The Binary Beasts"], downstream: ["The Codebreakers"], mission: "Developing and optimising algorithms for content recommendation and search.", techTags: ["Algorithms", "Python", "Machine Learning", "Search"] },
  { name: "The Binary Beasts", department: "xTV_Web", lead: "Charlotte Murphy", upstream: ["The Bit Manipulators"], downstream: ["The Algorithm Alliance"], mission: "Processing and transforming binary data formats for web streaming.", techTags: ["Binary Processing", "Streaming", "WebAssembly", "Codecs"] },
  { name: "The Error Handlers", department: "xTV_Web", lead: "Mia Henderson", upstream: ["The Feature Crafters"], downstream: ["The Debuggers"], mission: "Centralised error handling, logging, and alerting for xTV web services.", techTags: ["Error Handling", "Logging", "Alerting", "PagerDuty"] },
  { name: "Agile Avengers", department: "xTV_Web", lead: "Benjamin Hayes", upstream: ["The Scrum Lords"], downstream: ["The Sprint Kings"], mission: "Leading agile transformation and coaching for the xTV web division.", techTags: ["Agile", "SAFe", "Coaching", "Transformation"] },
  { name: "Bit Masters", department: "xTV_Web", lead: "Emma Richardson", upstream: ["The Debuggers"], downstream: ["API Avengers"], mission: "Low-level data processing and bit-stream management for web delivery.", techTags: ["Data Processing", "Bit Streams", "C++", "WebRTC"] },
  { name: "Byte Force", department: "xTV_Web", lead: "Elijah Parker", upstream: ["The Cloud Architects"], downstream: ["API Avengers"], mission: "Cloud-native byte processing and data transformation services.", techTags: ["Cloud Native", "Go", "Kubernetes", "Data Transform"] },
  { name: "Code Warriors", department: "xTV_Web", lead: "Olivia Carter", upstream: ["DevOps Dynasty"], downstream: ["The Debuggers"], mission: "Core feature development for Sky's xTV web streaming platform.", techTags: ["React", "TypeScript", "Streaming", "Web"] },
  { name: "DevOps Dynasty", department: "xTV_Web", lead: "Isabella Ross", upstream: ["The Jenkins Juggernauts"], downstream: ["Code Warriors"], mission: "DevOps infrastructure and platform engineering for xTV web services.", techTags: ["DevOps", "Terraform", "AWS", "Infrastructure"] },
  { name: "Full Stack Ninjas", department: "xTV_Web", lead: "Noah Campbell", upstream: ["The API Explorers", "The UX Wizards"], downstream: ["The API Explorers"], mission: "End-to-end full stack development for xTV web features and integrations.", techTags: ["Full Stack", "React", "Node.js", "PostgreSQL"] },
  { name: "Syntax Squad", department: "xTV_Web", lead: "Sophia Mitchell", upstream: ["The CI/CD Squad", "The Feature Crafters"], downstream: ["The Feature Crafters"], mission: "Code quality, linting, and syntax standards enforcement across xTV web.", techTags: ["Linting", "ESLint", "Prettier", "Code Standards"] },
  { name: "The Cloud Architects", department: "xTV_Web", lead: "Ava Sullivan", upstream: [], downstream: ["Byte Force", "Cache Me Outside"], mission: "Designing and managing cloud infrastructure architecture for xTV web.", techTags: ["AWS", "Cloud Architecture", "Terraform", "Networking"] },
  { name: "The Codebreakers", department: "xTV_Web", lead: "William Cooper", upstream: ["The Algorithm Alliance"], downstream: ["The Encryption Squad"], mission: "Security testing, penetration testing, and vulnerability assessment.", techTags: ["Security", "Pen Testing", "OWASP", "Vulnerability Scanning"], status: "Restructuring" },
  { name: "The Debuggers", department: "xTV_Web", lead: "James Bennett", upstream: ["Bug Exterminators", "Code Warriors", "Exception Catchers", "The Error Handlers"], downstream: ["Bit Masters"], mission: "Advanced debugging and root cause analysis for complex platform issues.", techTags: ["Debugging", "Root Cause Analysis", "Profiling", "APM"] },
];

export const teams: Team[] = teamDataRaw.map((t) => ({
  id: makeId(t.name),
  name: t.name,
  department: t.department,
  lead: t.lead,
  leadEmail: t.lead.toLowerCase().replace(" ", ".") + "@sky.uk",
  status: t.status || "Active",
  upstream: t.upstream,
  downstream: t.downstream,
  members: makeMembers(t.lead, t.name),
  mission: t.mission,
  slackChannel: makeSlack(t.name),
  email: makeEmail(t.name),
  repoUrl: "https://github.com/sky-uk/" + makeId(t.name),
  jiraUrl: "https://jira.sky.uk/browse/" + t.name.replace(/[^A-Z]/g, "").slice(0, 4),
  techTags: t.techTags,
  lastUpdatedBy: ["Zoey Stevens", "Henry Ward", "Sophia Mitchell", "James Bennett", "Isabella Ross"][Math.floor(t.name.length % 5)],
  lastUpdatedAt: ["2026-02-26 11:42", "2026-02-25 14:30", "2026-02-24 09:15", "2026-02-23 16:05", "2026-02-22 10:20"][Math.floor(t.name.length % 5)],
}));

export function getTeamById(id: string): Team | undefined {
  return teams.find((t) => t.id === id);
}

export function getTeamByName(name: string): Team | undefined {
  return teams.find((t) => t.name === name || t.name === "The " + name || "The " + t.name === name);
}

export function getTeamIdByName(name: string): string {
  const t = teams.find((tm) => tm.name === name);
  return t ? t.id : makeId(name);
}

export function getDepartmentForTeam(teamId: string): Department | undefined {
  return departments.find((d) => d.teamIds.includes(teamId));
}

export interface AuditEntry {
  id: string;
  action: string;
  target: string;
  user: string;
  timestamp: string;
}

export const auditLog: AuditEntry[] = [
  { id: "1", action: "Updated dependencies", target: "API Avengers", user: "Zoey Stevens", timestamp: "2026-02-26 11:42" },
  { id: "2", action: "Changed status to Restructuring", target: "The Codebreakers", user: "Henry Ward", timestamp: "2026-02-25 14:30" },
  { id: "3", action: "Updated team members", target: "The Feature Crafters", user: "Gabriel Coleman", timestamp: "2026-02-25 09:15" },
  { id: "4", action: "Updated contact channels", target: "The Debuggers", user: "James Bennett", timestamp: "2026-02-24 16:05" },
  { id: "5", action: "Added upstream dependency", target: "Cache Me Outside", user: "Owen Barnes", timestamp: "2026-02-24 10:20" },
  { id: "6", action: "Updated mission statement", target: "The UX Wizards", user: "Aurora Cooper", timestamp: "2026-02-23 15:30" },
  { id: "7", action: "Created team", target: "The Quantum Coders", user: "Bella Monroe", timestamp: "2026-02-22 11:00" },
  { id: "8", action: "Updated repo links", target: "DevOps Dynasty", user: "Isabella Ross", timestamp: "2026-02-21 09:45" },
  { id: "9", action: "Updated tech tags", target: "Syntax Squad", user: "Sophia Mitchell", timestamp: "2026-02-20 14:10" },
  { id: "10", action: "Removed team member", target: "The Sprint Kings", user: "Evelyn Hughes", timestamp: "2026-02-19 16:30" },
];

export interface Message {
  id: string;
  from: string;
  to: string;
  subject: string;
  body: string;
  timestamp: string;
  read: boolean;
}

export const messages: Message[] = [
  { id: "1", from: "Henry Ward", to: "You", subject: "API Avengers dependency update", body: "Hi, we've updated our upstream dependencies to include The Lambda Legends. Please review and confirm on your end.", timestamp: "2026-02-26 10:30", read: false },
  { id: "2", from: "Zoey Stevens", to: "You", subject: "Version control workflow changes", body: "We're rolling out a new branching strategy next sprint. Details attached.", timestamp: "2026-02-25 15:00", read: true },
  { id: "3", from: "Sophia Mitchell", to: "You", subject: "Code standards meeting", body: "Reminder: code standards review meeting tomorrow at 2pm.", timestamp: "2026-02-24 09:00", read: true },
];

export interface ScheduleEvent {
  id: string;
  title: string;
  team: string;
  date: string;
  time: string;
  description: string;
}

export const scheduleEvents: ScheduleEvent[] = [
  { id: "1", title: "Sprint Planning", team: "API Avengers", date: "2026-02-27", time: "10:00", description: "Sprint 24 planning session" },
  { id: "2", title: "Dependency Review", team: "The Feature Crafters", date: "2026-02-28", time: "14:00", description: "Quarterly dependency review" },
  { id: "3", title: "Retrospective", team: "The Debuggers", date: "2026-03-02", time: "11:00", description: "Sprint 23 retrospective" },
];
