<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Calculadora de Sección de Cable</title>
  <style>
    body { font-family: Arial, sans-serif; margin: 2em; background: #f4f4f4; }
    .container { background: #fff; padding: 2em; border-radius: 8px; max-width: 600px; margin: auto; box-shadow: 0 0 10px rgba(0,0,0,0.1); }
    h1 { text-align: center; }
    label { display: block; margin-top: 1em; }
    select, input, button { width: 100%; padding: 0.5em; margin-top: 0.5em; }
    #resultado { margin-top: 2em; background: #e6f7ff; padding: 1em; border-left: 4px solid #1890ff; }
  </style>
</head>
<body>
  <div class="container">
    <h1>Calculadora de Sección de Cable</h1>

    <label for="metodo">Método de instalación:</label>
    <select id="metodo">
      <option value="B1">B1</option>
    </select>

    <label for="tipo">Tipo de cable:</label>
    <select id="tipo">
      <option value="2xPVC">2xPVC</option>
      <option value="3xXLPE">3xXLPE</option>
    </select>

    <label for="longitud">Longitud del cable (m):</label>
    <input type="number" id="longitud" step="any">

    <label for="potencia">Potencia (W):</label>
    <input type="number" id="potencia" step="any">

    <label for="coseno">Cos φ:</label>
    <input type="number" id="coseno" step="any" value="0.9">

    <label for="material">Material:</label>
    <select id="material">
      <option value="CU">Cobre</option>
      <option value="AL">Aluminio</option>
    </select>

    <button onclick="calcularSeccion()">Calcular sección</button>

    <div id="resultado"></div>
  </div>

  <script>
    const tabla = {
      "B1": {
        "2xPVC": {
          1.5: 14.5, 2.5: 20, 4: 26, 6: 34, 10: 46, 16: 63, 25: 82, 35: 101, 50: 122, 70: 155, 95: 187, 120: 216, 150: 247, 185: 281, 240: 330
        },
        "3xXLPE": {
          1.5: 17.5, 2.5: 24, 4: 32, 6: 41, 10: 57, 16: 77, 25: 100, 35: 124, 50: 151, 70: 193, 95: 234, 120: 272, 150: 313, 185: 356, 240: 419
        }
      },
      "C": {
        "2xPVC": {
          1.5: 17, 2.5: 23, 4: 31, 6: 40, 10: 54, 16: 73, 25: 95, 35: 119, 50: 145, 70: 185, 95: 224, 120: 260, 150: 299, 185: 341, 240: 401
        },
        "3xXLPE": {
          1.5: 20, 2.5: 27, 4: 36, 6: 46, 10: 63, 16: 85, 25: 108, 35: 133, 50: 162, 70: 208, 95: 252, 120: 293, 150: 337, 185: 385, 240: 455
        }
      }
    };

    function calcularSeccion() {
      const metodo = document.getElementById('metodo').value;
      const tipo = document.getElementById('tipo').value;
      const L = parseFloat(document.getElementById('longitud').value);
      const W = parseFloat(document.getElementById('potencia').value);
      const COS = parseFloat(document.getElementById('coseno').value);
      const material = document.getElementById('material').value;

      const resultado = document.getElementById('resultado');
      const I = W / (230 * COS);

      const rho = material === 'CU' ? 0.0178 : 0.0282;

      const secciones = tabla[metodo][tipo];
      const sorted = Object.entries(secciones).sort((a,b) => parseFloat(a[0]) - parseFloat(b[0]));
      const encontrado = sorted.find(([seccion, intensidadMax]) => intensidadMax >= I);

      const intensidades_normalizadas = [10, 16, 20, 25, 32, 40, 50, 63];
      const I_normalizada = intensidades_normalizadas.find(i => i >= I);

      const S_teorica = (2 * rho * L * I * COS) / 2.3;
      const secciones_normalizadas = [1.5, 2.5, 4, 6, 10, 16, 25, 35, 50, 70, 95, 120, 150, 185, 240];
      const S_normalizada = secciones_normalizadas.find(s => s >= S_teorica);

      const Vd = (2 * rho * L * I * COS) / S_normalizada;
      const porcentaje = (Vd / 230) * 100;

      if (encontrado) {
        resultado.innerHTML = `
          ✅ Intensidad calculada: <strong>${I.toFixed(2)} A</strong><br>
          ✅ Intensidad normalizada (IGA): <strong>${I_normalizada} A</strong><br>
          ✅ Sección mínima según tabla: <strong>${encontrado[0]} mm²</strong> (soporta hasta ${encontrado[1]} A)<br>
          ✅ Sección teórica por caída de tensión: <strong>${S_teorica.toFixed(2)} mm²</strong><br>
          ✅ Sección normalizada: <strong>${S_normalizada} mm²</strong><br>
          ⚡ Caída de tensión: <strong>${Vd.toFixed(2)} V</strong><br>
          📉 Porcentaje de caída respecto a 230V: <strong>${porcentaje.toFixed(2)}%</strong>
        `;
      } else {
        resultado.innerHTML = `❌ Ninguna sección encontrada para ${I.toFixed(2)} A.`;
      }
    }
  </script>
</body>
</html>
