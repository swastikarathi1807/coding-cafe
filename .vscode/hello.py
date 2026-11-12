import json

# Load the file (adjust path if needed)
with open("ad-engagements.js", "r", encoding="utf-8") as f:
  content = f.read()

# Parse the JSON portion of the Twitter JS file
json_str = content[content.find("[") : content.rfind("]") + 1]
data = json.loads(json_str)

matching_ads_count = 0
advertisers = set()
advertiser_counts = {}

for entry in data:
  ad = entry.get("ad", entry)
  criteria_list = ad.get("matchedTargetingCriteria", [])

  matched = False
  current_advertiser = None

  for criterion in criteria_list:
    if "advertiserName" in criterion:
      current_advertiser = criterion["advertiserName"]

    if (
        criterion.get("targetingType") == "Interests"
        and criterion.get("targetingValue") == "Tax planning"
    ):
      matched = True

  if matched:
    matching_ads_count += 1
    if current_advertiser:
      advertisers.add(current_advertiser)
      advertiser_counts[current_advertiser] = (
          advertiser_counts.get(current_advertiser, 0) + 1
      )

print(f"a. How many ads matched: {matching_ads_count}")
print(f"b. How many different advertisers: {len(advertisers)}")
if advertiser_counts:
  top_advertiser = max(advertiser_counts, key=advertiser_counts.get)
  print(f"c. Top advertiser: {top_advertiser}")
