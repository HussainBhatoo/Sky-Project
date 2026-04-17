# Manual Test Plan & QA Registry
**Project:** Sky Engineering Team Registry (5COSC021W)
**Status:** [COMPLIANT] - Manual Verification Strategy
**Last Updated:** 2026-04-17

> [!IMPORTANT]
> **Rubric Compliance Note:** This project uses a **Manual Test Plan** approach as mandated by the CWK2 rubric ("Output of Test Plans"). Automated `tests.py` files have been removed to ensure the individual and group Word templates are the primary evidence of testing.

## 1. Testing Strategy
Students must perform manual verification for their specific modules and record results in the CWK2 Word template. Every test case must follow the structure below.

## 2. Global System Tests (Group)
| ID | Requirement | Test Action | Expected Result |
|:---|:---|:---|:---|
| **G-01** | Authentication | Attempt to visit `/dashboard/` without logging in. | Redirected to `/accounts/login/`. |
| **G-02** | Consistency | Navigate across all 5 modules. | Sidebar and styling remains 100% identical. |
| **G-03** | Search | Type "Streaming" into the global search bar. | Instant dropdown results show correct team links. |
| **G-04** | Audit Log | Edit a Team name and check the Audit Log page. | A new entry exists showing the change and actor. |

## 3. Module Specific Test Templates

### 3.1 Authentication & Profile (Maurya)
| ID | Title | Input | Expected Result |
|:---|:---|:---|:---|
| **A-01** | User Login | `maurya.patel` / `Sky1234!` | Success: Redirected to Dashboard with name in navbar. |
| **A-02** | Profile Update | Change Bio in Profile page. | Success message displayed; DB updated. |

### 3.2 Teams & Profiles (Riagul)
| ID | Title | Input | Expected Result |
|:---|:---|:---|:---|
| **T-01** | Team Discovery | Click a Team card on Dashboard. | Redirect to Team Detail showing full member list. |
| **T-02** | Disband Team | Click "Disband" on a team you manage. | Confirmation modal; Status changes to "Disbanded". |

### 3.3 Organisation & Dependencies (Lucas)
| ID | Title | Input | Expected Result |
|:---|:---|:---|:---|
| **O-01** | Org Chart | Click "Organisation" in sidebar. | Visual tree view of all departments and teams renders. |
| **O-02** | Dept Detail | Click "xTV_Web" department node. | Redirected to Department detail with team breakdown. |

### 3.4 Messaging Service (Suliman)
| ID | Title | Input | Expected Result |
|:---|:---|:---|:---|
| **M-01** | Send Message | Compose message to a team. | Message appears in "Sent" folder: Recipient sees in "Inbox". |
| **M-02** | Input Validation | Attempt to send an empty message. | Form error: "This field is required." |

### 3.5 Schedule & Logistics (Maurya)
| ID | Title | Input | Expected Result |
|:---|:---|:---|:---|
| **S-01** | Monthly View | Open Schedule module. | Full grid calendar renders for the current month. |
| **S-02** | Logic Check | End time earlier than Start time. | Form error: "End time cannot be before start time." |

### 3.6 Reports & Governance (Abdul-lateef)
| ID | Title | Input | Expected Result |
|:---|:---|:---|:---|
| **R-01** | CSV Export | Click "Export CSV". | A valid `.csv` file is downloaded with correct registry data. |
| **R-02** | Print Layout | Click "Print Report". | Browser print dialog opens with a clean layout (hidden sidebar/navbar). |
| **R-03** | Gap Analysis | Look at "Management Gaps". | Teams with no leader are highlighted in red as intended. |

---

## 4. How to Document Results (For Word Template)
Copy the table below into your Word document for each test case ran.

| Test Case ID | Test Result / Actual Outcome | Pass / Fail | Evidence (Screenshot) |
|:---:|:---|:---:|:---|
| **[ID]** | *e.g. Redirected to login as expected.* | **PASS** | Img_01.png |
