rem python -m pytest -s -v -m "sanity or regression" --html=./Reports/Report2.html testCases/ --browser chrome
rem pytest -s -v --html=Reports\Report.html testCases/ --browser chrome
rem pytest -s -v -m "sanity and regression" --html=./Reports/ReportChrome.html testCases/ --browser chrome
rem pytest -s -v -m "sanity or regression" --html=./Reports/ReportChrome.html testCases/ --browser chrome
python -m pytest -s -v -m "sanity or regression" --html=./Reports/ReportChrome.html testCases/test_login.py --browser chrome


rem python -m pytest -s -v -m "sanity" --html=./Reports/ReportFirefox.html testCases/ --browser firefox
rem pytest -s -v --html=Reports\Report.html testCases/ --browser firefox
rem pytest -s -v -m "sanity and regression" --html=./Reports/ReportFirefox.html testCases/ --browser firefox
rem pytest -s -v -m "sanity or regression" --html=./Reports/ReportFirefox.html testCases/ --browser firefox
python -m pytest -s -v -m "regression" --html=./Reports/ReportFirefox.html testCases/ --browser firefox

