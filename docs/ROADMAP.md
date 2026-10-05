# Scope and next steps

## Foundation delivered

Public home/about pages, roster and news empty states, joining information, and a public admin-status page. Plain static files are the proposed starter architecture; there is no server or database yet.

## Confirm before extending

1. Approved logo, Discord invite, social links, roster, photos, and publication consent.
2. Application questions, eligibility, moderation workflow, and retention/deletion expectations.
3. Hosting/runtime, database, Discord application ownership, callback URL, and authoritative administrator role policy.

## Discord login and admin boundary

Implement OAuth in a server-capable framework after the runtime is chosen. Use an authorization-code flow, validate state, keep client secrets and token exchange on the server, and use secure HttpOnly sessions with appropriate cookie and CSRF protections. Define minimal scopes and session expiry/logout behavior.

Enforce administrator permissions on every protected server route and mutation using a verified role/allowlist policy. Hiding navigation or checking a browser flag is not authorization. Do not populate the static admin-status page with private data. Test denied access, expired sessions, callback failures, and forged requests before enabling controls.

## Content and persistence

Publish confirmed roster and announcements first. Choose persistent storage before accepting applications or implementing admin edits. Validate submissions on the server and define access, moderation, and deletion behavior. Add photo uploads only with size/type validation and safe storage. Do not fabricate member statistics or treat sample data as live data.

Discord webhooks and live member counts are optional later work, requiring approved destinations and server-side credentials. They are not connected by this starter.

## Release criteria

Review mobile/desktop layouts, keyboard navigation, focus visibility, and contrast. Confirm all public content and links. Once a backend exists, test authentication and authorization and document its configuration separately. Configure deployment only after choosing a hosting target.
