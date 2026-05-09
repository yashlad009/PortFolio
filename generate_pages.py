import os

with open('base_template.html', 'r', encoding='utf-8') as f:
    template = f.read()

task_tracker_content = """
    <div class="section-header gs-reveal" style="margin-bottom: 64px;">
      <h2 class="section-title">Case Study: Task Tracker (APMS PRO)</h2>
    </div>

    <!-- 1. The Problem Statement -->
    <div class="project-card gs-project hoverable" style="flex-direction: column; padding: 40px; margin-bottom: 32px;">
      <h3 class="project-title" style="margin-bottom: 24px; color: var(--accent-cyan);">1. The Problem Statement</h3>
      <p class="project-desc" style="font-size: 16px;"><strong>Fragmentation:</strong> Users struggle to manage daily tasks, long-term milestones, and deadlines across multiple, disconnected apps.</p>
      <p class="project-desc" style="font-size: 16px;"><strong>Missing Intelligence:</strong> Traditional tools lack proactive guidance, resulting in overwhelmed users and missed deadlines.</p>
      <p class="project-desc" style="font-size: 16px; margin-bottom: 0;"><strong>Cognitive Load:</strong> Frequent app-switching kills focus and increases stress.</p>
    </div>

    <!-- 2. The Solution -->
    <div class="project-card gs-project hoverable" style="flex-direction: column; padding: 40px; margin-bottom: 32px;">
      <h3 class="project-title" style="margin-bottom: 24px; color: var(--accent-purple);">2. The Solution: Task Tracker</h3>
      <p class="project-desc" style="font-size: 16px;"><strong>THE Unified Platform:</strong> A full-featured web application that merges daily planning, project milestones, and AI mentorship into a single dashboard.</p>
      <p class="project-desc" style="font-size: 16px;"><strong>Dual-Portal Architecture:</strong> Features a User Portal for personal productivity and an Admin Portal for platform oversight and access control.</p>
      <p class="project-desc" style="font-size: 16px; margin-bottom: 0;"><strong>Secure Onboarding:</strong> Implementation of secure registration using OTP email verification and admin key-based access.</p>
    </div>

    <!-- 3. Key Technical Pillars -->
    <div class="project-card gs-project hoverable" style="flex-direction: column; padding: 40px; margin-bottom: 32px;">
      <h3 class="project-title" style="margin-bottom: 24px; color: var(--accent-cyan);">3. Key Technical Pillars</h3>
      <p class="project-desc" style="font-size: 16px;"><strong>Gamified Logic:</strong> A "Token Engine" that rewards task completion, allowing users to earn Bronze, Silver, and Gold achievement certificates to sustain motivation.</p>
      <p class="project-desc" style="font-size: 16px;"><strong>High-Precision Reminders:</strong> A backend scheduling engine that sends automated 30-minute email alerts for high-priority tasks.</p>
      <p class="project-desc" style="font-size: 16px;"><strong>Visual Progress Tracking:</strong> Real-time gradient progress bars for long-term milestones, providing instant visual feedback on goal completion.</p>
      <p class="project-desc" style="font-size: 16px; margin-bottom: 0;"><strong>Performance Analytics:</strong> A dedicated dashboard surfacing metrics like Efficiency % and task productivity charts to identify user roadblocks.</p>
    </div>

    <!-- 4. The AI Advantage -->
    <div class="project-card gs-project hoverable" style="flex-direction: column; padding: 40px; margin-bottom: 32px;">
      <h3 class="project-title" style="margin-bottom: 24px; color: var(--accent-purple);">4. The AI Advantage (TaskTracker AI)</h3>
      <p class="project-desc" style="font-size: 16px;"><strong>Context-Aware Mentorship:</strong> Unlike generic chatbots, the AI analyzes the user's actual tasks, milestones, and career level to provide strategic advice.</p>
      <p class="project-desc" style="font-size: 16px;"><strong>Intelligent Prioritization:</strong> Users can request real-time guidance on what to prioritize based on their current workload and deadlines.</p>
      <p class="project-desc" style="font-size: 16px; margin-bottom: 0;"><strong>Actionable Strategies:</strong> The mentor identifies specific blockers and suggests leveling-up strategies to help users climb from "Bronze" to "Elite" status.</p>
    </div>

    <!-- 5. Conclusion & Impact -->
    <div class="project-card gs-project hoverable" style="flex-direction: column; padding: 40px; margin-bottom: 32px;">
      <h3 class="project-title" style="margin-bottom: 24px; color: var(--accent-cyan);">5. Conclusion & Impact</h3>
      <p class="project-desc" style="font-size: 16px;"><strong>Target Audience:</strong> Built specifically for students, professionals, and teams seeking to reclaim control over their time.</p>
      <p class="project-desc" style="font-size: 16px; margin-bottom: 0;"><strong>Outcome:</strong> APMS PRO transforms task management from a passive recording activity into an active, gamified journey toward professional achievement.</p>
    </div>
"""

study_stack_content = """
    <div class="section-header gs-reveal" style="margin-bottom: 64px;">
      <h2 class="section-title">Case Study: Study Stack</h2>
    </div>

    <!-- 1. The Core Problem -->
    <div class="project-card gs-project hoverable" style="flex-direction: column; padding: 40px; margin-bottom: 32px;">
      <h3 class="project-title" style="margin-bottom: 24px; color: var(--accent-cyan);">1. The Core Problem: "The Student Paradox"</h3>
      <p class="project-desc" style="font-size: 16px;">Students juggle multiple high-stakes domains (academics, social life, personal growth) without the formal project management training found in the corporate world.</p>
      <p class="project-desc" style="font-size: 16px;"><strong>Pain Points:</strong> Procrastination, "Academic Burnout," fragmented schedules, and the inability to visualize long-term progress.</p>
      <p class="project-desc" style="font-size: 16px; margin-bottom: 0;"><strong>The Gap:</strong> Most apps are either too simple (Notes) or too complex (Jira/Asana). This project requires a student-centric middle ground.</p>
    </div>

    <!-- 2. Feature Breakdown & Logic -->
    <div class="project-card gs-project hoverable" style="flex-direction: column; padding: 40px; margin-bottom: 32px;">
      <h3 class="project-title" style="margin-bottom: 24px; color: var(--accent-purple);">2. Feature Breakdown & Logic</h3>
      <ul class="tl-desc" style="font-size: 16px;">
        <li style="font-size: 16px; margin-bottom: 12px;"><strong>Task & Timetable:</strong> Conflict detection between classes and assignment deadlines.</li>
        <li style="font-size: 16px; margin-bottom: 12px;"><strong>Progress Tracking:</strong> Visual "completion bars" or Pomodoro-style session logging.</li>
        <li style="font-size: 16px; margin-bottom: 12px;"><strong>Goal Setting:</strong> Breaking "Big Goals" (e.g., Final Exams) into "Micro-tasks."</li>
        <li style="font-size: 16px; margin-bottom: 12px;"><strong>Analytics:</strong> Data on "Peak Productivity Hours" and time distribution per subject.</li>
        <li style="font-size: 16px; margin-bottom: 0;"><strong>Reporting:</strong> Daily/Weekly summaries to reflect on missed vs. achieved targets.</li>
      </ul>
    </div>

    <!-- 3. Targeted User Personas -->
    <div class="project-card gs-project hoverable" style="flex-direction: column; padding: 40px; margin-bottom: 32px;">
      <h3 class="project-title" style="margin-bottom: 24px; color: var(--accent-cyan);">3. Targeted User Personas</h3>
      <p class="project-desc" style="font-size: 16px;"><strong>The Overwhelmed Achiever:</strong> Has 100 tasks; needs prioritization and a clear "next step."</p>
      <p class="project-desc" style="font-size: 16px;"><strong>The Procrastinator:</strong> Needs "nudge" notifications and gamified rewards to stay focused.</p>
      <p class="project-desc" style="font-size: 16px; margin-bottom: 0;"><strong>The Visual Learner:</strong> Relies on the Analytics dashboard to see where their time actually goes.</p>
    </div>

    <!-- 4. Technical & Design Considerations -->
    <div class="project-card gs-project hoverable" style="flex-direction: column; padding: 40px; margin-bottom: 32px;">
      <h3 class="project-title" style="margin-bottom: 24px; color: var(--accent-purple);">4. Technical & Design Considerations</h3>
      <p class="project-desc" style="font-size: 16px;"><strong>UI/UX:</strong> Minimalism is vital. If the app is hard to use, it becomes another "task" rather than a solution.</p>
      <p class="project-desc" style="font-size: 16px;"><strong>Engagement:</strong> Use Push Notifications strategically (avoiding "notification fatigue").</p>
      <p class="project-desc" style="font-size: 16px;"><strong>Data Integrity:</strong> Secure storage for academic schedules and progress data.</p>
      <p class="project-desc" style="font-size: 16px; margin-bottom: 0;"><strong>The "Success" Metric:</strong> A successful solution isn't just an app that records data, but one that changes behavior. If a student can identify that they are 30% more productive on Tuesday mornings than Friday nights, the app has succeeded.</p>
    </div>
"""

task_tracker_html = template.replace('<!-- CONTENT_PLACEHOLDER -->', task_tracker_content)
study_stack_html = template.replace('<!-- CONTENT_PLACEHOLDER -->', study_stack_content)

with open('task-tracker-case-study.html', 'w', encoding='utf-8') as f:
    f.write(task_tracker_html)

with open('study-stack-case-study.html', 'w', encoding='utf-8') as f:
    f.write(study_stack_html)
