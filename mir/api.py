from rest_framework import viewsets
from opal.core.views import json_response
from rest_framework.permissions import IsAuthenticated


class MirApi(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)

    def dispatch(self, *args, **kwargs):
        self.name = kwargs.pop('name', 'pathway')
        self.incident_id = kwargs.get('incident_id', None)
        return super(MirApi, self).dispatch(*args, **kwargs)

    def retrieve(self, *args, **kwargs):
        return json_response({
            "timeline":
            {
                "headline":"Whitney Houston<br/> 1963 - 2012",
                "startDate":"1963",
                "text":"<p>Houston's voice caught the imagination of the world propelling her to superstardom at an early age becoming one of the most awarded performers of our time. This is a look into the amazing heights she achieved and her personal struggles with substance abuse and a tumultuous marriage.</p>",
                "type":"default",
                "asset":
                {
                    "media":"//www.flickr.com/photos/tm_10001/2310475988/",
                    "credit":"flickr/<a href='http://www.flickr.com/photos/tm_10001/'>tm_10001</a>",
                    "caption":"Whitney Houston performing on her My Love is Your Love Tour in Hamburg."
                },
                "date": [
                    {
                        "startDate":"1963,8,9",
                        "headline":"A Musical Heritage",
                        "text":"<p>Born in New Jersey on August 9th, 1963, Houston grew up surrounded by the music business. Her mother is gospel singer Cissy Houston and her cousins are Dee Dee and Dionne Warwick.</p>",
                        "asset":
                        {
                            "media":"{{ static_url }}/img/examples/houston/family.jpg",
                            "credit":"Cissy Houston photo:<a href='http://www.flickr.com/photos/11447043@N00/418180903/'>Tom Marcello</a><br/><a href='http://commons.wikimedia.org/wiki/File%3ADionne_Warwick_television_special_1969.JPG'>Dionne Warwick: CBS Television via Wikimedia Commons</a>",
                            "caption":"Houston's mother and Gospel singer, Cissy Houston (left) and cousin Dionne Warwick."
                        }
                    },
                    {
                        "startDate":"1978",
                        "headline":"First Recording",
                        "text":"At the age of 15 Houston was featured on Michael Zager's song, Life's a Party.",
                        "asset":
                        {
                            "media":"https://youtu.be/fSrO91XO1Ck",
                            "credit":"<a href=\"http://unidiscmusic.com\">Unidisc Music</a>",
                            "caption":""
                        }
                    },
                     {
                        "startDate":"1978",
                        "headline":"The Early Years",
                        "text":"As a teen Houston's credits include background vocals for Jermaine Jackson, Lou Rawls and the Neville Brothers. She also sang on Chaka Khan's, 'I'm Every Woman,' a song which she later remade for the <i>Bodyguard</i> soundtrack which is the biggest selling soundtrack of all time. It sold over 42 million copies worldwide.",
                        "asset":
                        {
                            "media":"https://youtu.be/_gvJCCZzmro",
                            "credit":"EbonyJet",
                            "caption":"A young poised Whitney Houston in an interview with EbonyJet."
                        }
                    },
                    {
                        "startDate":"1978",
                        "headline":"Early Album Credits",
                        "text":"As a teen Houston's credits include background vocals for Jermaine Jackson, Lou Rawls and the Neville Brothers. She also sang on Chaka Khan's, 'I'm Every Woman,' a song which she later remade for the <i>Bodyguard</i> soundtrack which is the biggest selling soundtrack of all time. It sold over 42 million copies worldwide.",
                        "asset":
                        {
                            "media":"https://youtu.be/H7_sqdkaAfo",
                            "credit":"Arista Records",
                            "caption":"I'm Every Women as performed by Whitney Houston."
                        }
                    },
                    {
                        "startDate":"1983",
                        "headline":"Signed",
                        "text":"Houston is signed to Arista Records after exec Clive Davis sees her performing on stage with her mother in New York.",
                        "asset":
                        {
                            "media":"https://youtu.be/A4jGzNm2yPI",
                            "credit":"Sony Music Entertainment",
                            "caption":"Whitney Houston and Clive Davis discussing her discovery and her eponymous first album."
                        }
                    },
                     {
                        "startDate":"1985",
                        "headline":"Debut",
                        "text":"Whitney Houston's self titled first release sold over 12 million copies in the U.S. and included the hit singles 'How Will I Know,' 'You Give Good Love,' 'Saving All My Love For You' and 'Greatest Love of All.'",
                        "asset":
                        {
                            "media":"https://youtu.be/m3-hY-hlhBg",
                            "credit":"Arista Records Inc.",
                            "caption":"The 'How Will I Know' video showcases the youthful energy that boosted Houston to stardom."
                        }
                    },
                    {
                        "startDate":"1986",
                        "headline":"'The Grammys'",
                        "text":"In 1986 Houston won her first Grammy for the song Saving All My Love. In total she has won six Grammys, the last of which she won in 1999 for It's Not Right But It's Okay.",
                        "asset":
                        {
                            "media":"https://youtu.be/v0XuiMX1XHg",
                            "credit":"<a href='http://grammy.org'>The Recording Academy</a>",
                            "caption":"Dionne Warwick gleefully announces cousin, Whitney Houston, the winner of the Best Female Pop Vocal Performance for the song Saving All My Love."
                        }
                    },
                    {
                        "startDate":"1987",
                        "headline":"'Whitney'",
                        "text":"Multiplatinum second album sells more than 20 million copies worldwide. With 'Whitney', Houston became the first female artist to produce four number 1 singles on one album including \"I Wanna Dance With Somebody,' 'Didn't We Almost Have It All,' 'So Emotional' and 'Where Do Broken Hearts Go.'",
                        "asset":
                        {
                            "media":"https://youtu.be/eH3giaIzONA",
                            "credit":"Arista Records Inc.",
                            "caption":"I Wanna Dance With Somebody"
                        }
                    },
                    {
                        "startDate":"1988",
                        "headline":"\"One Moment In Time\"",
                        "text":"The artist's fame continues to skyrocket as she records the theme song for the Seoul Olympics, 'One Moment In Time.'",
                        "asset":
                        {
                            "media":"https://youtu.be/96aAx0kxVSA",
                            "credit":"Arista Records Inc.",
                            "caption":"\"One Moment In Time\" - Theme song to the 1988 Seoul Olympics"
                        }
                    },
                    {
                        "startDate":"1989",
                        "headline":"Bobby Brown",
                        "text":"Houston and Brown first meet at the Soul Train Music Awards. In an interview with Rolling Stone Magazine, Houston admitted that it was not love at first sight. She turned down Brown's first marriage proposal but eventually fell in love with him.",
                        "asset":
                        {
                            "media":"",
                            "credit":"",
                            "caption":""
                        }
                    },
                    {
                        "startDate":"1991",
                        "headline":"Super Bowl",
                        "text":"Houston's national anthem performance captures the hearts and minds of Americans ralllying behind soldiers in the Persian Guf War.",
                        "asset":
                        {
                            "media":"https://youtu.be/5Fa09teeaqs",
                            "credit":"CNN",
                            "caption":"CNN looks back at Houston's iconic performance of the national anthem at Superbowl XXV."
                        }
                    },
                    {
                        "startDate":"1992",
                        "headline":"\"The Bodyguard\"",
                        "text":"Houston starred opposite Kevin Costner in the box office hit, The Bodyguard. The soundtrack to the movie sold over 44 million copies worldwide  garnering 3 Grammy's for the artist.",
                        "asset":
                        {
                            "media":"https://youtu.be/h9rCobRl-ng",
                            "credit":"Arista Records",
                            "caption":"\"Run To You\" from the 1992 \"Bodyguard\" soundtrack.."
                        }
                    },
                    {
                        "startDate":"1992",
                        "headline":"Married Life",
                        "text":"<p>After three years of courtship, Houston marries New Edition singer Bobby Brown. Their only child Bobbi Kristina Brown was born in 1993.</p><p>In 2003 Brown was charged with domestic violence after police responded to a domestic violence call. Houston and Brown were featured in the reality show, \"Being bobby Brown,\" and divorced in 2007.</p>",
                        "asset":
                        {
                            "media":"https://youtu.be/5cDLZqe735k",
                            "credit":"",
                            "caption":"Bobby Brown performing \"My Prerogrative,\" from his \"Don't be Cruel\" solo album. Bobby Brown first became famous with the R&B group, New Edition."
                        }
                    },
                    {
                        "startDate":"2002",
                        "headline":"Crack is Whack",
                        "text":"<p>Houston first publicly admitted to drug use in an interview with Diane Sawyer. The singer coined the term \"Crack is Whack,\" saying that she only used more expensive drugs.</p>",
                        "asset":
                        {
                            "media":"//upload.wikimedia.org/wikipedia/commons/d/dd/ABC_-_Good_Morning_America_-_Diane_Sawyer.jpg",
                            "credit":"flickr/<a href='http://www.flickr.com/photos/23843757@N00/194521206/'>Amanda Benham</a>",
                            "caption":"Diane Sawyer "
                        }
                    },

                    {
                        "startDate":"2004",
                        "headline":"Rehab",
                        "text":"<p>Houston entered rehab several times beginning in 2004. She declared herself drug free in an interview with Oprah Winfrey in 2009 but returned to rehab in 2011.</p>",
                        "asset":
                        {
                            "media":"https://youtu.be/KLk6mt8FMR0",
                            "credit":"CNN",
                            "caption":"Addiction expert, Dr. Drew, talks about Whitney's death and her struggle with addiction."
                        }
                    },
                    {
                        "startDate":"2005",
                        "headline":"Being Bobby Brown",
                        "text":"<p>Being Bobby Brown was a reality show starring Brown and wife Whitney Houston. Houston refused to sign for a second season. A clip of her telling Brown to \"Kiss my ass,\" became a running gag on The Soup.</p>",
                        "asset":
                        {
                            "media":"",
                            "credit":"",
                            "caption":""
                        }
                    },
                    {
                        "startDate":"2010",
                        "headline":"A Rocky Comeback",
                        "text":"<p>Houston's comeback tour is cut short due to a diminished voice damaged by years of smoking. She was reportedly devastated at her inability to perform like her old self.</p>",
                        "asset":
                        {
                            "media":"",
                            "credit":"",
                            "caption":""
                        }
                    },
                    {
                        "startDate":"2012,2,11",
                        "headline":"Whitney Houston<br/> 1963-2012",
                        "text":"<p>Houston, 48, was discovered dead at the Beverly Hilton Hotel on  on Feb. 11, 2012. She is survived by her daughter, Bobbi Kristina Brown, and mother, Cissy Houston.</p>",
                        "asset":
                        {
                            "media":"//twitter.com/Blavity/status/851872780949889024",
                            "credit":"<a href='http://commons.wikimedia.org/wiki/File%3AFlickr_Whitney_Houston_performing_on_GMA_2009_4.jpg'>Asterio Tecson</a> via Wikimedia",
                            "caption":"Houston, performing on Good Morning America in 2009."
                        }

                    }
                ]
            }
        })
