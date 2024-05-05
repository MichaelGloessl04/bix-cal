<template>
  <div id="app">
    <RouterView />
  </div>
</template>

<style>
.hover-box {
  min-width: 10rem;
  display: flex;
  justify-content: center;
  align-items: center;
  width: 20rem;
  margin: 1rem;
  padding: 1rem;
  border-radius: 1rem;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.61);
  position: absolute;
  z-index: 9999;
}
</style>
