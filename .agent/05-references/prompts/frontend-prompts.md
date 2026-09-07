# Frontend Prompts — General Frontend Prompts

> Ready-to-use prompts for any frontend stack.

---

## 1. Creating a CRUD page
```
Create a management page for [Entity] containing:
- A data table with: search, filtering, sorting, pagination
- A create/edit form with: instant validation, clear error messages
- Delete confirmation with a warning message
- States: loading (skeleton), empty (empty state), error

Comply with: responsive design + accessibility + no business logic in components
```

## 2. UX improvement
```
Improve the user experience on this screen: [screen]

Verify:
- Buttons disabled during processing with a loading indicator
- Clear success/error messages
- Responsive on phone and tablet
- Empty states with a suggested action
- Confirmation before destructive operations
```

## 3. Creating a reusable component
```
Create reusable component [ComponentName]:
- Inputs (Props/Inputs): [list]
- Outputs (Events/Outputs): [list]
- States: normal, loading, error, disabled

The component must be: self-contained, testable, documented
```

## 4. Fixing a rendering problem
```
This screen has a problem: [problem description]

Verify:
- Browser console errors
- Network tab: does the data arrive correctly?
- Does the problem occur in all browsers or just one?
- Is it related to screen size?
```
