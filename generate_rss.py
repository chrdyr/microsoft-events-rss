import feedparser
import xml.etree.ElementTree as ET
import datetime

# Hämta och filtrera från ett externt RSS-flöde
source_url = "https://techcommunity.microsoft.com/gxcuf89792/rss/filteredbylabel?label=Events"
feed = feedparser.parse(source_url)

# Skapa RSS-rot
rss = ET.Element("rss", version="2.0")
channel = ET.SubElement(rss, "channel")

ET.SubElement(channel, "title").text = "Microsoft Events – Digital Arbetsplats"
ET.SubElement(channel, "link").text = "https://events.microsoft.com"
ET.SubElement(channel, "description").text = "Filtrerade Microsoft-events för Copilot, M365, Viva, etc."
ET.SubElement(channel, "language").text = "sv-SE"
ET.SubElement(channel, "lastBuildDate").text = datetime.datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S +0000")

# Filtrera relevanta event
keywords = ["copilot", "microsoft 365", "digital workplace", "power platform", "viva", "sharepoint", "ignite"]
for entry in feed.entries:
    if any(kw.lower() in entry.title.lower() or kw.lower() in entry.summary.lower() for kw in keywords):
        item = ET.SubElement(channel, "item")
        ET.SubElement(item, "title").text = entry.title
        ET.SubElement(item, "link").text = entry.link
        ET.SubElement(item, "description").text = entry.summary
        ET.SubElement(item, "pubDate").text = entry.published

# Spara som XML
tree = ET.ElementTree(rss)
tree.write("feed.xml", encoding="utf-8", xml_declaration=True)
