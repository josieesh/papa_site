class Section:
    def __init__(self, id, name, text):
        self.id = id
        self.name = name
        self.link = name.replace(" ", "_")
        self.text = text
        self.child_sections = []

def sortContents(textFiles):
    first_level = dict()
    second_level = dict()
    third_level = dict()
    fourth_level = dict()
    for tf in textFiles:
        newSection = Section(tf.id, tf.name, tf.text)
        if tf.heading_level == 1:
            first_level[tf.id] = newSection
        elif tf.heading_level == 2:
            first_level[tf.parent_page.id].child_sections.append(newSection)
            second_level[tf.id] = newSection
        elif tf.heading_level == 3:
            second_level[tf.parent_page.id].child_sections.append(newSection)
            third_level[tf.id] = newSection
        else:
            third_level[tf.parent_page.id].child_sections.append(newSection)
            fourth_level[tf.id] = newSection

    return {"level1": first_level, "level2": second_level, "level3": third_level, "level4": fourth_level}


