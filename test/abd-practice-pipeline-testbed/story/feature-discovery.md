---
abd_pipeline:
  # override: this doc auto-saves the graph without prompting
  md_to_json: yes
target_skill: skills/story-driven-delivery/abd-story-mapping
---

# Feature: Trip Booking — Story Map Outline (sample)

> Sample deliverable for the **abd-practice-pipeline** testbed.
> Drives `abd-story-mapping` end-to-end: rules pass → scanner pass → JSON → drawio.

## Context

Customers planning a multi-leg trip want to compare options, hold an itinerary, and pay in
one flow. We are mapping the **happy path** at story-map outline depth (Level 1).

## Map (verb–noun)

### Epic: Search trips
- Sub-epic: Build query
  - Story: Pick origin and destination
  - Story: Choose dates
  - Story: Set passenger count
- Sub-epic: Browse results
  - Story: View result list
  - Story: Filter by price
  - Story: Sort by duration

### Epic: Hold itinerary
- Sub-epic: Compose itinerary
  - Story: Add outbound leg
  - Story: Add return leg
  - Story: Reserve hold (15 minutes)

### Epic: Pay and confirm
- Sub-epic: Capture payment
  - Story: Enter card details
  - Story: Apply promo code
- Sub-epic: Confirm booking
  - Story: Receive confirmation email
  - Story: View booking in account
