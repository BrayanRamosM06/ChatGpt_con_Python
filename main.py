import openai
import config
import typer
from rich import print
from rich.table import Table
#creamos la key par que nos de el acceso al asistende de IA



def main():

  openai.api_key = config.api_key
  
  #hacemos que la termanl sea de una manera mas visible
  print ("[bold green] Interactuar con ChatGpt con Python[/bold green]")

  table = Table("Comando", "Descripción")
  table.add_row("Exit", "para salir de la apliacación")
  table.add_row("new", "Creamos una nueva conversación")
  print (table)

  #este es el contexto del aasistente
  context = {"role":"system", "content": "Eres un asistente muy útil"}
  messages = [context]

  while True:
 
   content = __prompt()

   if content =="new":
      print(" 🆕 nueva conversación")
      messages = [context]
      content = __prompt() 

     #Agregamos al array mas preguntas 
   messages.append( {"role":"user", "content": content })

   response = openai.ChatCompletion.create(
     model="gpt-3.5-turbo", messages=messages)
   
   response_content = response.choices[0].message.content

   messages.append({"role":"assistant","content":response_content})


   print(f"[bold green]> [/bold green] [green]{response_content}[/green]")

def __prompt() -> str:
    
  prompt = typer.prompt("\n¿De qué quieres hablar ahora? ")

  if prompt  == "Exit":
    exit = typer.confirm(" 🤚Estas seguro de que quieres salir del programa")
    if exit:
      print(" 🖐 hasta luego¡¡¡¡")
      raise typer.Abort()
    
    return __prompt()
  
  return prompt 

if __name__ == "__main__":
   typer.run(main)