from django import template


register = template.Library()



def spotme(author, me):
  '''
  me is a single name
  author is a string containing names including me
  This function return author string with <span></span> around me
  '''
  return author.replace(me, f"<span>{me}</span>")


register.filter("spotme",spotme)

