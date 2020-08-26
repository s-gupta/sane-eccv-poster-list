# export n=spotlights
# grep uk-link-toggle $n-list.htm > $n-links.txt
# grep Spotlight $n-list.htm > $n-id.txt
# grep uk-text-italic $n-list.htm > $n-authors.txt
# grep h4 $n-list.htm > $n-title.txt

# export m=authors
export m=id
cat orals-$m.txt spotlights-$m.txt poster-$m.txt > $m.txt
