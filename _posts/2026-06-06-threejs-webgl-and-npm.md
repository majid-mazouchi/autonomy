---
title: "Three.js, WebGL & npm — A Plain-Words Monograph"
subtitle: "Three names you meet on day one of web 3D — what each one actually is, how they fit together, and the practical notes nobody tells you up front."
date: 2026-06-06 23:00:00 -0400
category: "Tools"
slug: threejs-webgl-and-npm
excerpt: "WebGL is the low-level graphics API your browser exposes for talking to the GPU. Three.js is the library that hides 800 lines of WebGL boilerplate behind a 30-line scene-camera-renderer setup. npm is the package manager that gets Three.js into your project in one command. The three are almost always introduced together and almost never explained clearly. This monograph fixes that — with a rotating cube you can poke, a worked example that builds a scene from scratch, and the practical notes about performance, shaders, and the tooling ecosystem."
reading_time: 18
---

There is a particular kind of web tutorial that introduces *Three.js, WebGL, and npm* as if they were three peers, then proceeds to use all three without ever explaining what role each is playing. They are not peers. WebGL is a low-level graphics API the browser exposes. Three.js is a library that wraps WebGL into something humans actually want to write. npm is how you install Three.js. The relationship is "WebGL is the GPU. Three.js is the steering wheel. npm is the car dealership." Once you have that picture, the rest of the web-3D landscape stops looking like a hall of mirrors.

This monograph is the plain-English version, written for the developer who can write JavaScript and has been meaning to learn 3D but keeps bouncing off tutorials that assume too much. The headline figure is a rotating wireframe cube that you can poke — its speed and rotation rate are sliders in the page — and the math behind it is the math WebGL is running on your GPU as you read this.

## What it covers

About eighteen minutes of reading, plus whatever time you spend playing with the demos.

**§ 1 — The three things, in one breath.** WebGL = the API, Three.js = the library, npm = the package manager. The relationship in one sentence each.

**§ 2 — WebGL, in plain words.** What the GPU actually does. Vertex shaders, fragment shaders, the rasterization pipeline. Why "raw WebGL" is famously painful (it isn't *bad* — it's just the wrong abstraction for application code).

**§ 3 — Three.js, in plain words.** What the library actually gives you. Scene, camera, renderer, mesh, material, light. The minimum-viable Three.js scene in thirty lines.

**§ 4 — npm, the third leg.** How packages get into your project. `npm install three`. Why this is the easiest of the three to use and the easiest of the three to mess up. Cross-reference to the [Node.js & npm]({{ '/posts/nodejs-and-npm/' | relative_url }}) post for the deeper treatment.

**§ 5 — The worked example: a rotating cube.** Step by step. The HTML page. The npm install. The scene-camera-renderer setup. The animation loop. The cube. The lights. The orbit controls. About 60 lines of code from empty folder to working interactive 3D scene.

**§ 6 — Shaders, briefly.** What you'd write if you decided to leave Three.js and use WebGL directly. The vertex shader. The fragment shader. The GLSL language. When this is worth doing and when it isn't.

**§ 7 — Performance notes.** The handful of mistakes that tank a 3D web app. Recreating geometries every frame. Loading uncompressed textures. Forgetting to dispose of resources. The four-rule discipline that catches most of it.

**§ 8 — The wider ecosystem.** What lives around Three.js. **react-three-fiber** for React users. **Babylon.js** as the leading alternative library. **WebGPU** as the next-generation API replacing WebGL.

**§ 9 — Further reading.** The Three.js docs, the WebGL fundamentals tutorials, and the handful of YouTube creators who teach this well.

## Read it

<div style="margin: 28px 0; text-align: center;">
  <a href="{{ '/assets/posts/threejs-webgl-and-npm.html' | relative_url }}"
     style="display: inline-block; padding: 14px 28px; background: var(--accent); color: var(--paper); font-family: var(--f-ui); font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; text-decoration: none; border-radius: 2px; font-weight: 500;">
    Open the monograph →
  </a>
</div>

The monograph lives at its own URL with a warm-paper layout — burnt-orange Three.js accent, crimson npm accent, an interactive rotating cube in the hero that you can speed up and slow down.

---

← Back to [Autonomy]({{ '/' | relative_url }})
