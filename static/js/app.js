document.addEventListener("DOMContentLoaded", () => {
  const sidebar = document.getElementById("sidebar");
  const open = document.getElementById("openSidebar");
  const close = document.getElementById("closeSidebar");
  const toggle = document.getElementById("toggleSidebar");
  if (open && sidebar) open.addEventListener("click", () => sidebar.classList.add("open"));
  if (close && sidebar) close.addEventListener("click", () => sidebar.classList.remove("open"));
  if (toggle) toggle.addEventListener("click", () => document.body.classList.toggle("sidebar-collapsed"));
});
