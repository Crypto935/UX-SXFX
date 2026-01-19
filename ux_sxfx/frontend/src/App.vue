<script setup lang="ts">
import { ref, onMounted } from 'vue';
import './assets/estilos.css';
const sidebarOpen = ref(false); 

const toggleSidebar = () => {
  sidebarOpen.value = !sidebarOpen.value;
};

const menuItems = [
  { title: 'Principal', icon: 'home', subItems: ['Dashboard', 'Equipos Asignados', 'Proyectos', 'Requisiciones'] },
  { title: 'Mantenimiento', icon: 'tool', subItems: ['Programa Semanal', 'Backlog', 'Reservas'] },
  { title: 'Mensajes', icon: 'message', subItems: ['Entrada', 'Enviados', 'Sistema'] },
  { title: 'Equipos', icon: 'list', subItems: ['Todos los Equipos', 'Áreas', 'Materiales'] },
  { title: 'Reportes', icon: 'report', subItems: ['Reportes Generales'] }
];

// --- Esto es puro Backend ---
const usuario = ref({ nombre: '', cargo: '', pendientes: 0 });
const actividades = ref([]);

const cargarDashboard = async () => {
  try {
    const respuesta = await fetch('http://localhost:8000/api/dashboard/');
    if (!respuesta.ok) throw new Error('Error al conectar con Django');
    const datos = await respuesta.json();
    usuario.value = datos.usuario;
    actividades.value = datos.actividades;
  } catch (error) {
    console.error('Error cargando datos:', error);
  }
};

onMounted(() => {
  cargarDashboard();
});
</script>
// ---Aqui ya es Frontend ---
<template>
  <div class="layout">
    
    <aside class="sidebar" :class="{ 'expanded': sidebarOpen }">
      <div class="sidebar-header">
        <div class="toggle-btn" @click="toggleSidebar" title="Alternar Menú">
           <svg viewBox="0 0 24 24" width="24" height="24" stroke="white" stroke-width="2" fill="none"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>
        </div>
        <div class="brand-title" v-show="sidebarOpen">
          <span>ESDE III</span>
          <span class="brand-subtitle">▼</span>
        </div>
      </div>

      <div class="menu-items">
        <div v-for="(item, index) in menuItems" :key="index" class="menu-group">
          <div class="group-header" :class="{ 'active-group': index === 0 }">
            <div class="icon-placeholder">
              <svg v-if="item.icon === 'home'" viewBox="0 0 24 24" width="20" height="20" stroke="currentColor" fill="none"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path></svg>
              <svg v-else-if="item.icon === 'tool'" viewBox="0 0 24 24" width="20" height="20" stroke="currentColor" fill="none"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"></path></svg>
              <svg v-else-if="item.icon === 'message'" viewBox="0 0 24 24" width="20" height="20" stroke="currentColor" fill="none"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg>
              <svg v-else-if="item.icon === 'list'" viewBox="0 0 24 24" width="20" height="20" stroke="currentColor" fill="none"><rect x="3" y="3" width="7" height="7"></rect><rect x="14" y="3" width="7" height="7"></rect><rect x="14" y="14" width="7" height="7"></rect><rect x="3" y="14" width="7" height="7"></rect></svg>
              <svg v-else viewBox="0 0 24 24" width="20" height="20" stroke="currentColor" fill="none"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>
            </div>
            <span class="group-title" v-show="sidebarOpen">
              {{ item.title }} 
              <span class="arrow">▼</span>
            </span>
          </div>
          <div class="sub-items" v-if="sidebarOpen">
            <div v-for="sub in item.subItems" :key="sub" class="sub-link" :class="{'active-link': sub === 'Dashboard'}">
              {{ sub }}
            </div>
          </div>
        </div>
      </div>
      
      <div class="sidebar-footer">
        <button class="btn-nuevo" v-show="sidebarOpen">Nuevo ▼</button>
        <div class="logout-box">
           <div class="icon-placeholder"><svg viewBox="0 0 24 24" width="20" height="20" stroke="currentColor" stroke-width="2" fill="none"><path d="M18.36 6.64a9 9 0 1 1-12.73 0"></path><line x1="12" y1="2" x2="12" y2="12"></line></svg></div>
           <button class="btn-logout-text" v-show="sidebarOpen">Cerrar Sesión</button>
        </div>
      </div>
    </aside>

    <main class="main-content">
      <div class="top-bar">
        <h1 class="logo-text">SXFX <span class="gear-icon">⚙️</span></h1>
        <div class="top-icons"><span>🔔</span><span>✉️</span><div class="user-circle">👤</div></div>
      </div>
      <div class="red-header-bg"><div class="marca-agua">GRUPO MÉXICO MINERÍA</div></div>
      <div class="cards-container">
        <div class="card user-card">
          <div class="avatar-circle">
            <svg viewBox="0 0 24 24" width="40" height="40" stroke="#555" stroke-width="1.5" fill="none"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
          </div>
          <div class="user-info"><h2>{{ usuario.nombre }}</h2><p class="role">{{ usuario.cargo }}</p><p class="pendientes">Pendientes: <strong>#{{ usuario.pendientes }}</strong></p></div>
        </div>
        <div class="card activity-card">
          <div class="card-header"><h3>Actividad Reciente</h3><span>≡</span></div>
          <div class="card-body scrollable">
            <div class="timeline">
              <div v-for="item in actividades" :key="item.id" class="timeline-item">
                <div class="time-col">{{ item.tiempo }}</div>
                <div class="dot-col"><span class="dot" :style="{ backgroundColor: item.color }"></span><div class="line"></div></div>
                <div class="text-col">{{ item.texto }}</div>
              </div>
            </div>
            <div class="card-actions"><button class="btn-red">Ver Más</button><button class="btn-red">Bitácora</button></div>
          </div>
        </div>
        <div class="card poblada-card">
          <div class="card-header"><h3>Poblada</h3><span>≡</span></div>
          <div class="card-body"><p style="color: #666; font-size: 0.9rem;">Hace 10 min</p><div class="spacer"></div><button class="btn-red full-width">Poblar</button></div>
        </div>
      </div>
    </main>
  </div>
</template>