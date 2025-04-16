import { useState } from "react";
import { Card, CardContent } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table";
import { Trash2 } from "lucide-react";

const circuitosBase = [
  { nombre: "C1", intensidad: 10, seccion: 1.5 },
  { nombre: "C2", intensidad: 16, seccion: 2.5 },
  { nombre: "C3", intensidad: 25, seccion: 6 },
  { nombre: "C4", intensidad: 16, seccion: 2.5 },
  { nombre: "C5", intensidad: 16, seccion: 2.5 },
  { nombre: "C6", intensidad: 25, seccion: 6 },
  { nombre: "C7", intensidad: 16, seccion: 2.5 },
  { nombre: "C8", intensidad: 16, seccion: 2.5 },
  { nombre: "C9", intensidad: 20, seccion: 4 },
  { nombre: "C10", intensidad: 25, seccion: 6 },
  { nombre: "C11", intensidad: 25, seccion: 6 },
  { nombre: "C12", intensidad: 25, seccion: 6 },
  { nombre: "C13", intensidad: 25, seccion: 6 }
];

const letras = ["", "A", "B", "C"];
const circuitos = circuitosBase.flatMap(c => letras.map(l => ({
  nombre: c.nombre + l,
  intensidad: c.intensidad,
  seccion: c.seccion
})));

const resistividad = 0.0175; // Ohm·mm²/m para cobre
const tension = 230; // Voltios
const seccionesNormalizadas = [1.5, 2.5, 4, 6, 10, 16, 25, 35, 50];

function calcularCaida(intensidad, seccion, longitud) {
  const R = (resistividad * longitud * 2) / seccion; // ida y vuelta
  const V = intensidad * R;
  const porcentaje = (V / tension) * 100;
  return { V: V.toFixed(2), porcentaje: porcentaje.toFixed(2) };
}

function calcularAlternativa(intensidad, longitud) {
  for (const s of seccionesNormalizadas) {
    const { porcentaje } = calcularCaida(intensidad, s, longitud);
    if (parseFloat(porcentaje) <= 3) {
      const resultado = calcularCaida(intensidad, s, longitud);
      return { seccion: s, ...resultado };
    }
  }
  return null;
}

export default function ITC25Calculator() {
  const [seleccion, setSeleccion] = useState("");
  const [longitud, setLongitud] = useState("");
  const [resultados, setResultados] = useState([]);

  const calcular = () => {
    const nombreInput = seleccion.toUpperCase().trim();
    const circuito = circuitos.find(c => c.nombre === nombreInput);
    if (!circuito || !longitud) return;
    const { V, porcentaje } = calcularCaida(
      circuito.intensidad,
      circuito.seccion,
      Number(longitud)
    );
    let alternativo = null;
    if (parseFloat(porcentaje) > 3) {
      alternativo = calcularAlternativa(circuito.intensidad, Number(longitud));
    }
    setResultados([
      ...resultados,
      {
        ...circuito,
        nombre: nombreInput,
        longitud: Number(longitud),
        V,
        porcentaje,
        alternativo
      }
    ]);
    setLongitud("");
    setSeleccion("");
  };

  const eliminarCircuito = (idx) => {
    setResultados(resultados.filter((_, i) => i !== idx));
  };

  return (
    <div className="p-4 space-y-4">
      <Card>
        <CardContent className="space-y-4 p-4">
          <div className="space-y-2">
            <label className="block font-semibold">Nombre del circuito</label>
            <Input
              type="text"
              placeholder="Ej: C1, C1A, C13C..."
              value={seleccion}
              onChange={(e) => setSeleccion(e.target.value)}
            />
          </div>
          <div className="space-y-2">
            <label className="block font-semibold">Longitud en metros</label>
            <Input
              type="number"
              placeholder="Longitud"
              value={longitud}
              onChange={(e) => setLongitud(e.target.value)}
            />
          </div>
          <Button onClick={calcular}>Añadir circuito</Button>
        </CardContent>
      </Card>

      {resultados.length > 0 && (
        <Table>
          <TableHeader>
            <TableRow>
              <TableHead>Circuito</TableHead>
              <TableHead>Intensidad (A)</TableHead>
              <TableHead>Longitud (m)</TableHead>
              <TableHead>Sección (mm²)</TableHead>
              <TableHead>Caída V (V)</TableHead>
              <TableHead>Caída %</TableHead>
              <TableHead></TableHead>
            </TableRow>
          </TableHeader>
          <TableBody>
            {resultados.map((r, idx) => (
              <>
                <TableRow key={`${r.nombre}-${idx}`} className={parseFloat(r.porcentaje) > 3 ? "bg-red-100" : ""}>
                  <TableCell>{r.nombre}</TableCell>
                  <TableCell>{r.intensidad}</TableCell>
                  <TableCell>{r.longitud}</TableCell>
                  <TableCell>{r.seccion}</TableCell>
                  <TableCell>{r.V}</TableCell>
                  <TableCell>{r.porcentaje}</TableCell>
                  <TableCell>
                    <Button variant="ghost" size="icon" onClick={() => eliminarCircuito(idx)}>
                      <Trash2 className="h-4 w-4" />
                    </Button>
                  </TableCell>
                </TableRow>
                {r.alternativo && (
                  <TableRow className="bg-green-50">
                    <TableCell>{r.nombre} (ajustado)</TableCell>
                    <TableCell>{r.intensidad}</TableCell>
                    <TableCell>{r.longitud}</TableCell>
                    <TableCell>{r.alternativo.seccion}</TableCell>
                    <TableCell>{r.alternativo.V}</TableCell>
                    <TableCell>{r.alternativo.porcentaje}</TableCell>
                    <TableCell></TableCell>
                  </TableRow>
                )}
              </>
            ))}
          </TableBody>
        </Table>
      )}
    </div>
  );
}
