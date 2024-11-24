from bs4 import BeautifulSoup

# Your HTML content
html_content = """
<lib-bewerberdetail-kopfbereich _ngcontent-ng-c2221240997="" _nghost-ng-c2442096492="" class="ng-star-inserted"><article _ngcontent-ng-c2442096492="" class="ba-layout-tile hyphenate ng-star-inserted"><div _ngcontent-ng-c2442096492="" class="kopfzeile-topline greytext"><span _ngcontent-ng-c2442096492="" id="detail-kopfbereich-suchttext" _msttexthash="244205" _msthash="10">Searches job as:</span></div><h2 _ngcontent-ng-c2442096492="" id="detail-kopfbereich-titel" class="ba-heading" _msttexthash="462007" _msthash="11">Clinical psychologist</h2><ul _ngcontent-ng-c2442096492="" class="tag-list"><li _ngcontent-ng-c2442096492="" id="detail-kopfbereich-verfuegbarkeit" class="tag-small tag-blue"><font _mstmutation="1" _msttexthash="97279" _msthash="12">As of now</font><!----></li><li _ngcontent-ng-c2442096492="" class="tag-small tag-blue ng-star-inserted" id="detail-kopfbereich-arbeitszeit-0" _msttexthash="114985" _msthash="13">Full time</li><!----></ul><hr _ngcontent-ng-c2442096492=""><div _ngcontent-ng-c2442096492="" aria-hidden="true" class="tag-list lokation-icon"><span _ngcontent-ng-c2442096492="" class="tag-small ba-icon ba-icon-location-full"></span><ul _ngcontent-ng-c2442096492="" class="tag-list lokation-list"><li _ngcontent-ng-c2442096492="" id="detail-kopfbereich-lokation-0" class="ng-star-inserted" _msttexthash="95953" _msthash="14">Germany</li><!----><!----></ul></div><div _ngcontent-ng-c2442096492="" id="detail-kopfbereich-erwartung-stelle" class="ba-copytext beschreibung ng-star-inserted"><p _ngcontent-ng-c2442096492="" _msttexthash="140400" _msthash="15">IncomingCC</p></div><!----><!----><!----><!----><!----></article><!----></lib-bewerberdetail-kopfbereich>
<span _ngcontent-ng-c394748106="" title="Ausbildung:" aria-label="Ausbildung:" role="img" class="bi-mortarboard-fill tag-icon" _msthidden="1" _mstaria-label="170027" _msthash="19" _msttexthash="746473">​</span>
"""

# Create a BeautifulSoup object and parse the HTML content
soup = BeautifulSoup(html_content, 'lxml')

# Extract job title/position
job_title = soup.find('h2', {'id': 'detail-kopfbereich-titel'}).text.strip()

# Extract years of experience
# Assuming it's mentioned in the description or another tag in the actual document,
# here we are assuming it's stored in the `div` with `id='detail-kopfbereich-erwartung-stelle'` for this example.
years_of_experience = soup.find('div', {'id': 'detail-kopfbereich-erwartung-stelle'}).text.strip()

# Extract education (degree)
# Assuming it's stored in a <span> with title or aria-label containing 'Ausbildung' 
education = soup.find('span', {'title': 'Ausbildung:'})['aria-label']

# Print the results
print(f"Job Title: {job_title}")
print(f"Years of Experience: {years_of_experience}")
print(f"Education: {education}")
