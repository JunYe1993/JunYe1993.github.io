import markdownify as h2m
import tool.html2markdown.getLocalFile as local
import tool.html2markdown.html2text.html2text as old_h2m
import tool.html2markdown.html2markdown.html2markdown as oldold_h2m


if __name__ == "__main__":
    # get local data
    h_map = local.getHtmlMap()
    m_map = local.getMarkdownMap()

    # check if there are html file not converted yet.
    newMd = []
    existMd = set(m_map['post'])
    for htmlFile in h_map['post']:
        if htmlFile not in existMd:
            newMd.append(htmlFile)

    # convert
    count = 0
    for md in newMd:
        # read html file
        htmlData = ""
        try:
            with open ("./article/" + md + ".html", "r") as htmlFile:
                htmlData = htmlFile.read()
        except:
            print("Read ./article/" + md + ".html failed")
            break  

        # write converted markdown file
        mdData = h2m.markdownify(htmlData)
        try:
            with open ("./article/" + md + ".md", "w") as mdFile:
                mdFile.write(mdData) 
        except:
            print("Write ./article/" + md + ".md failed")
            break

        local.saveMarkdownMap(m_map, md)
        # break # for test
        count += 1
        print("Progress: "+str(count)+"/"+str(len(newMd)))
                 
