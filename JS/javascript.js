function aumentarImagem(elemento) {
    elemento.style.transform = 'scale(1,5)';
  }
  
  function normalizarImagem(elemento) {
    elemento.style.transform = 'scale(1)';
  }
  function showProject(event,projectNumber) {
    event.preventDefault();
    // Oculta todos os projetos
    var projects = document.querySelectorAll('.box');
    projects.forEach(function(project) {
      project.style.display = 'none';
    });
  
    // Mostra o projeto específico
    var selectedProject = document.getElementById('project-' + projectNumber);
    selectedProject.style.display = 'flex';
  }
  