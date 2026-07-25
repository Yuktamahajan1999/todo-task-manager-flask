// Instant Search & Filter Logic
function filterTasks() {
    const searchVal = document.getElementById('searchInput').value.toLowerCase();
    const priorityVal = document.getElementById('priorityFilter').value;
    const cards = document.querySelectorAll('.task-card');

    cards.forEach(card => {
        const textData = card.getAttribute('data-title') || '';
        const priorityData = card.getAttribute('data-priority') || '';

        const matchesSearch = textData.includes(searchVal);
        const matchesPriority = priorityVal === 'ALL' || priorityData === priorityVal;

        if (matchesSearch && matchesPriority) {
            card.style.display = 'flex';
        } else {
            card.style.display = 'none';
        }
    });
}

// Edit Modal Handler with Due Date Support
function openEditModal(id, title, description, priority, dueDate) {
    const modal = document.getElementById('editModal');
    const form = document.getElementById('editForm');

    form.action = `/edit/${id}`; // Ensure this matches your Flask route
    document.getElementById('edit_title').value = title;
    document.getElementById('edit_description').value = description;
    document.getElementById('edit_priority').value = priority;
    document.getElementById('edit_due_date').value = dueDate;

    modal.style.display = 'flex';
}

function closeEditModal() {
    document.getElementById('editModal').style.display = 'none';
}