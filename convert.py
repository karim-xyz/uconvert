import typer
from rich import print
from typing_extensions import Annotated

app = typer.Typer(no_args_is_help=True)

length_units = {
  "nm": 1e-09,
  "um": 1e-06,
  "mm": 0.001,
  "cm": 0.01,
  "m": 1,
  "km": 1000,
  "in": 0.0254,
  "ft": 0.3048
}

area_units = {
  "mm2": 1e-06,
  "cm2": 0.0001,
  "m2": 1,
  "km2": 1000000,
  "ha": 10000,
  "in2": 0.00064516,
  "ft2": 0.09290304
}

mass_units = {
  "mg": 1e-6,
  "g": 0.001,
  "kg": 1,
  "t": 1000,
  "oz": 0.0283495,
  "lb": 0.453592,
  "t_us": 907.1847
}

volume_units = {
  "mm3": 1e-9,
  "cm3": 1e-6,
  "m3": 1,
  "km3": 1e9,
  "l": 0.001,
  "ml": 1e-6,
  "gal": 0.00378541
}

@app.command()
def length(value: Annotated[float, typer.Argument()],
          base_unit: Annotated[str, typer.Argument()], 
          result_unit: Annotated[str, typer.Argument()]
          ):
            if base_unit in length_units and result_unit in length_units:
              r = (value*length_units[base_unit])*(1/length_units[result_unit])
              if str(r)[-2:] == ".0":
                r = int(r)
              print(r)
            elif base_unit not in length_units and result_unit in length_units:
              print(f"[red]Invalid unit: {base_unit}[/red]")
            elif result_unit not in length_units and base_unit in length_units:
              print(f"[red]Invalid unit: {result_unit}[/red]")
            else:
              print(f"[red]Invalid units: {base_unit}, {result_unit}[/red]")

@app.command()
def area(value: Annotated[float, typer.Argument()],
          base_unit: Annotated[str, typer.Argument()], 
          result_unit: Annotated[str, typer.Argument()]
          ):
            if base_unit in area_units and result_unit in area_units:
              r = (value*area_units[base_unit])*(1/area_units[result_unit])
              if str(r)[-2:] == ".0":
                r = int(r)
              print(r)
            elif base_unit not in area_units and result_unit in area_units:
              print(f"[red]Invalid unit: {base_unit}[/red]")
            elif result_unit not in area_units and base_unit in area_units:
              print(f"[red]Invalid unit: {result_unit}[/red]")
            else:
              print(f"[red]Invalid units: {base_unit}, {result_unit}[/red]")

@app.command()
def mass(value: Annotated[float, typer.Argument()],
          base_unit: Annotated[str, typer.Argument()], 
          result_unit: Annotated[str, typer.Argument()]
          ):
            if base_unit in mass_units and result_unit in mass_units:
              r = (value*mass_units[base_unit])*(1/mass_units[result_unit])
              if str(r)[-2:] == ".0":
                r = int(r)
              print(r)
            elif base_unit not in mass_units and result_unit in mass_units:
              print(f"[red]Invalid unit: {base_unit}[/red]")
            elif result_unit not in mass_units and base_unit in mass_units:
              print(f"[red]Invalid unit: {result_unit}[/red]")
            else:
              print(f"[red]Invalid units: {base_unit}, {result_unit}[/red]")

@app.command()
def volume(value: Annotated[float, typer.Argument()],
          base_unit: Annotated[str, typer.Argument()], 
          result_unit: Annotated[str, typer.Argument()]
          ):
            if base_unit in volume_units and result_unit in volume_units:
              r = (value*volume_units[base_unit])*(1/volume_units[result_unit])
              if str(r)[-2:] == ".0":
                r = int(r)
              print(r)
            elif base_unit not in volume_units and result_unit in volume_units:
              print(f"[red]Invalid unit: {base_unit}[/red]")
            elif result_unit not in volume_units and base_unit in volume_units:
              print(f"[red]Invalid unit: {result_unit}[/red]")
            else:
              print(f"[red]Invalid units: {base_unit}, {result_unit}[/red]")

@app.command()
def units():
  categories = {"Length Units": length_units, "Area Units": area_units, "Mass Units": mass_units, "Volume Units": volume_units}
  for category, units in categories.items():
    print(category)
    print(", ".join(units.keys()))
    print()

if __name__ == "__main__":
  app()
