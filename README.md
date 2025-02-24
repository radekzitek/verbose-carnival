# Verbose Carnival Project

## Project Overview

This is a Vue.js 3 application that utilizes state-of-the-art tools and components, including:
- Vue.js 3, Vue CLI, Vue Router
- Pinia for state management
- Vite for building and bundling
- Material Design for Bootstrap (MDB Vue UI Kit) for UI components and styling

## Key Improvements and Considerations

### General
- **Consistent Styling:** All views and components have been migrated to use MDB components for a unified look.
- **Code Formatting:** Use Prettier (or a similar tool) to maintain consistent code formatting.
- **Component Structure:** Components are broken down into smaller, reusable parts (e.g., AppHeader, AppSidebar, AppFooter, AppMain).
- **Error Handling & Accessibility:** Enhanced error handling (especially in API calls) along with proper use of semantic HTML and ARIA attributes.
- **Security:** Considerations for secure handling of user credentials and tokens (e.g., password hashing and secure token storage) are noted.

### Specific Files and Components

- **AppHeader.vue:** 
  - Uses MDB components (MDBContainer, MDBRow, MDBCol, MDBBtn, MDBIcon) and router-links for navigation.
  - Menu items change dynamically based on the authentication state.

- **AppSidebar.vue:** 
  - Displays a list of external references using MDB grid components.
  - Images and texts are presented with a consistent layout.

- **AppFooter.vue:** 
  - A simple footer using MDBFooter, displaying copyright.

- **AppMain.vue:** 
  - Wraps the routed content inside an MDBContainer for a fluid layout.

- **LoginView.vue:** 
  - Provides a login form built with MDB components.
  - Includes fields for Username and Password, along with a link to password recovery.
  
- **RegisterView.vue:** 
  - Registration form capturing Username, Email, First Name, Last Name, Password, and Verify Password.
  - Uses MDB forms and grid layout for a clean interface.

- **ContactView.vue:** 
  - Displays contact information using MDB layout components.
  - Contains email and additional placeholder text.

- **AboutView.vue:** 
  - Contains detailed Lorem Ipsum placeholder text describing the project.
  - Includes a router-link for navigating to the Contact page.

- **NotFoundView.vue:** 
  - Custom 404 page built with MDB components.
  - Provides a user-friendly message with a link to return to the home page.

## Libraries Used

- **mdb-vue-ui-kit:** Material Design components for Vue.js enhancing the UI with prebuilt elements.

## Project Structure

The project follows a conventional Vue CLI layout:
- `src/` — Source code
  - `components/` — Reusable Vue components (e.g., AppHeader, AppSidebar, AppFooter, AppMain)
  - `views/` — Route-specific pages (e.g., LoginView, RegisterView, ContactView, AboutView, NotFoundView)
  - `assets/` — Images and other static files
  - `stores/` — Pinia stores for state management
  - `router/` — Vue Router configuration
  - `App.vue` — The root component

## Getting Started

1. **Clone the repository:**
   ```bash
   git clone <repository_url>
   ```
2. **Install dependencies:**
   ```bash
   npm install
   # or using yarn:
   yarn install
   ```
3. **Run the development server:**
   ```bash
   npm run serve
   # or using yarn:
   yarn serve
   ```

## Future Considerations

- **Form Reusability:** Extract common logic from LoginView and RegisterView into a reusable form component.
- **Validation:** Integrate a robust validation library like VeeValidate or Yup.
- **Security Enhancements:** Improve handling of sensitive data (e.g., token storage and password hashing).
- **Configuration:** Consider externalizing menu and sidebar configuration for easier maintenance.

## Workspace Reference

This workspace has been updated with MDB-based components for a cohesive design:
- **AppHeader.vue, AppSidebar.vue, AppFooter.vue, AppMain.vue**: Core layout components using MDB.
- **LoginView.vue & RegisterView.vue**: Authentication views built with MDB inputs, buttons, and card layouts.
- **ContactView.vue, AboutView.vue, NotFoundView.vue**: Informational views using MDB design elements.

Happy coding!