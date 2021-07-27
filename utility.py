
def diplay_skills(skillcategories,subcategories, skills):

  total_skill = {}

  for category in skillcategories:
    skill_dico = {}
    total_skill[category.category_name] = {}

    for subcategorie in subcategories:
      print(subcategorie.subcategory_name)
      skill_dico[subcategorie.subcategory_name] = []

      for skill in skills:
        if skill.category.category_name == category.category_name:
          if skill.subcategory:
            if skill.subcategory.subcategory_name == subcategorie.subcategory_name:
              skill_dico[subcategorie.subcategory_name].append(skill.name)
          else:
            skill_dico[skill.name] = skill.name

    # remove empty value
    skill_dico = dict( [(key_skill,skills_list) for key_skill,skills_list in skill_dico.items() if len(skills_list)>0])
    total_skill[category.category_name] = skill_dico

  return total_skill


