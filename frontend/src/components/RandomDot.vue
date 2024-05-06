<template>
    <div
      v-for="(dot, index) in dots"
      :key="index"
      class="dot"
      :style="{ top: dot.top + 'px', left: dot.left + 'px' }"
    ></div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        dots: [],
        mousePosition: { x: 0, y: 0 },
        avoidanceStrength: 50 // Adjust the strength of avoidance
      };
    },
    mounted() {
      this.generateDots();
      window.addEventListener("mousemove", this.updateMousePosition);
    },
    destroyed() {
      window.removeEventListener("mousemove", this.updateMousePosition);
    },
    methods: {
      generateDots() {
        const padding = 5;
        const coverage = 400;
        const windowWidth = window.innerWidth - padding;
        const windowHeight = window.innerHeight - padding;
        const numDots = Math.floor((windowWidth * windowHeight) / coverage);
  
        const gridSize = Math.sqrt((windowWidth * windowHeight) / numDots);
        const gridOffset = gridSize / 2;
  
        const strength = 0.5;
  
        for (let i = 0; i < numDots; i++) {
          const row = Math.floor(i / (windowWidth / gridSize));
          const col = i % (windowWidth / gridSize);
          const x =
            col * gridSize +
            (Math.random() * gridSize - gridOffset) * strength;
          const y =
            row * gridSize +
            (Math.random() * gridSize - gridOffset) * strength;
  
          this.dots.push({ top: y, left: x });
        }
      },
      updateMousePosition(event) {
        this.mousePosition = { x: event.clientX, y: event.clientY };
        this.updateDotPositions();
      },
      updateDotPositions() {
        for (let i = 0; i < this.dots.length; i++) {
          const dot = this.dots[i];
          const distanceX = dot.left - this.mousePosition.x;
          const distanceY = dot.top - this.mousePosition.y;
          const distance = Math.sqrt(distanceX ** 2 + distanceY ** 2);
          if (distance < this.avoidanceStrength) {
            const angle = Math.atan2(distanceY, distanceX);
            const newX =
              dot.left + Math.cos(angle) * this.avoidanceStrength;
            const newY =
              dot.top + Math.sin(angle) * this.avoidanceStrength;
            this.$set(this.dots, i, { top: newY, left: newX });
          }
        }
      }
    }
  };
  </script>
  
  <style lang="scss">
  $dot-size: 3.5px;
  
  .dot {
    width: $dot-size;
    height: $dot-size;
    background-color: rgb(66, 76, 83);
    border-radius: 50%;
    position: fixed;
    z-index: 999;
    transition: transform 0.1s;
  }
  </style>
  