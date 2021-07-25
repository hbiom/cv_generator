

def spot_me(author, me):
  '''
  me is a single name
  author is a string containing names including me
  This function return author string with <span></span> around me
  '''
  return author.replace(me, f"<span>{me}</span>")


# skill_list = diplay_skills(skillcategories, Subcategory.objects.all(), skills)


def diplay_skills(skillcategories,subcategories, skills):

  total_skill = {}

  for category in skillcategories:
    skill_dico = {}
    total_skill[category.category_name] = {}

    for subcategorie in subcategories:
      #skill_dico[subcategorie.subcategory_name] = []
      skill_dico[subcategorie.subcategory_name] = ''

      for skill in skills:
        if skill.category.category_name == category.category_name:
          if skill.subcategory:
            print(skill.category.category_name + ':' + category.category_name)

            if skill.category.category_name == category.category_name:
              #skill_dico[subcategorie.subcategory_name].append(skill.name)
              skill_dico[subcategorie.subcategory_name] += f'{skill.name} '
          else:
            skill_dico[skill.name] = skill.name

    total_skill[category.category_name] = skill_dico

  return total_skill


