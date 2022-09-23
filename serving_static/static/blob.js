import { spline } from 'https://cdn.skypack.dev/@georgedoescode/spline@1.0.1'
import SimplexNoise from 'https://cdn.skypack.dev/simplex-noise@2.4.0'


const path = document.querySelector("path")
const root = document.documentElement

let hueNoiseOffset = 0
let originalStep = 0.0002
let noiseStep = originalStep * document.getElementById("speed").value


const simplex = new SimplexNoise()
const points = createPoints();

(function animate() {
    path.setAttribute("d", spline(points, 1, true))
    noiseStep = originalStep * document.getElementById("speed").value
    for (let i = 0; i < points.length; i++) {
        const point = points[i]

        const nX = noise(point.noiseOffsetX, point.noiseOffsetX)
        const nY = noise(point.noiseOffsetY, point.noiseOffsetY)

        const x = map(nX, -1, 1, point.originX - 20, point.originX + 20)
        const y = map(nY, -1, 1, point.originY - 20, point.originY + 20)

        point.x = x
        point.y = y

        point.noiseOffsetX += noiseStep
        point.noiseOffsetY += noiseStep
    }

    root.style.setProperty("#DDD", `hsl(186, 48, 53, 100%, 75%)`)
    root.style.setProperty("#333", `hsl(186, 48, 53, 100%, 75%)`)

    hueNoiseOffset += noiseStep / 6

    requestAnimationFrame(animate)
})();

function map(n, start1, end1, start2, end2) {
    return ((n - start1) / (end1 - start1)) * (end2 - start2) + start2
}

function noise(x, y) {
    return simplex.noise2D(x, y)
}

function createPoints() {
    const points = []

    const numPoints = 6;//change number of Points here
    const angleStep = (Math.PI * 2) / numPoints
    const rad = 75

    for (let i = 1; i <= numPoints; i++) {
        // x & y coordinates of the current point
        const theta = i * angleStep

        const x = 100 + Math.cos(theta) * rad
        const y = 100 + Math.sin(theta) * rad

        // store the point's position
        points.push({
            x: x,
            y: y,
            // reference point's original point for modulate values later
            originX: x,
            originY: y,

            noiseOffsetX: Math.random() * 1000,
            noiseOffsetY: Math.random() * 1000
        });
    }
    return points
}

function rgb2hsv (r, g, b) {
    let rabs, gabs, babs, rr, gg, bb, h, s, v, diff, diffc, percentRoundFn
    rabs = r / 255
    gabs = g / 255
    babs = b / 255
    v = Math.max(rabs, gabs, babs),
        diff = v - Math.min(rabs, gabs, babs)
    diffc = c => (v - c) / 6 / diff + 1 / 2
    percentRoundFn = num => Math.round(num * 100) / 100
    if (diff === 0)
        h = s = 0
    else {
        s = diff / v
        rr = diffc(rabs)
        gg = diffc(gabs)
        bb = diffc(babs)

        if (rabs === v)
            h = bb - gg
        else if (gabs === v)
            h = (1 / 3) + rr - bb
        else if (babs === v)
            h = (2 / 3) + gg - rr
        if (h < 0)
            h += 1
        else if (h > 1)
            h -= 1
    }
    return {
        h: Math.round(h * 360),
        s: percentRoundFn(s * 100),
        v: percentRoundFn(v * 100)
    }
}//https://stackoverflow.com/questions/8022885/rgb-to-hsv-color-in-javascript

function moveBlob(target, i){
    let w_w
    let h_h
    if (Math.round(Math.random()) === 1)
        w_w = "-"
    else
        w_w = ""
    if (Math.round(Math.random()) === 1)
        h_h = "-"
    else
        h_h = ""
    target.style.transform =
        "translate("
        + w_w + Math.random()*600+1 + "px, "
        + h_h + Math.random()*300+1 + "px) rotate("
        + Math.random()*360+ "deg)"
    return i++
}


window.onload = function(){
    let target = document.getElementsByTagName("svg")[0]
    let render_rate = 30*1000
    let i = 0

    setInterval(function(){
        i = moveBlob(target, i)
    },render_rate)
}

document.querySelector("path").addEventListener("mouseover", () => {//hover effect (rare)
    noiseStep = originalStep * document.getElementById("speed").value *10
});
document.querySelector("path").addEventListener("mouseleave", () => {
    noiseStep = originalStep * document.getElementById("speed").value
});