<template>
  <div id="app">
    <header>
      <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container-fluid">
          <router-link to="/" class="navbar-brand">Bixcal</router-link>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav">
              <li class="nav-item">
                <router-link to="/" class="nav-link">Home</router-link>
              </li>
              <li class="nav-item">
                <router-link to="/people" class="nav-link">People</router-link>
              </li>
              <li class="login">
                <router-link to="/login" class="nav-link">
                  <i class="bi bi-person-fill"></i>
                </router-link>
              </li>
            </ul>
          </div>
        </div>
      </nav>
    </header>
    <body>
      <RouterView />
    </body>
  </div>
</template>

<style>
.hover-box {
  background-color: rgb(49, 49, 49);
  min-width: 10rem;
  width: 20rem;
  height: auto;
  display: flex;
  justify-content: center;
  align-items: center;
  position: fixed;
  top: 20%;
  left: 50%;
  transform: translate(-50%, -50%);
  padding: 1em;
  border-radius: 1rem;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.61);
  z-index: 9999;
}

.login {
  font-size: 160%;
  position: absolute;
  right: 0;
  top: 0;
  padding: 0 1rem;
}
</style>
