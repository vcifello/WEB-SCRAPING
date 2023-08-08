from parsel import Selector

def get_opponents(html):
    selector = Selector(text=html)

    matches = selector.xpath('//table[@class="wikitable"]')[0]
    trs = matches.xpath(".//tr")

    opponents = []

    for tr in trs[1:]:
        opponent = {
            'link': None,
            'name': None,
            'outcome': None,
        }

        opponent['outcome'] = tr.xpath("./td[1]/text()").get().strip("\n")
        opponents_node = tr.xpath("./td[3]")
        anchors = opponents_node.xpath("a")
        if len(anchors) == 1:
            a= anchors[0]
            href = a.xpath("@href").get()
            opponent['link'] = f"https://en.wikipedia.org{href}"
            opponent_name = a.xpath("text()").get()
        else:
            opponent_name = opponents_node.xpath("text()").get()

        opponent['name'] = opponent_name.strip('\n')
        opponents.append(opponent)

    return  opponents
