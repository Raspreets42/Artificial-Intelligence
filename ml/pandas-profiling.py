import pandas as pd
from ydata_profiling import ProfileReport

data = {
    'companies': ['TCS', 'Accenture', 'Wipro', 'Cognizant', 'Capgemini', 'HDFC Bank', 'Infosys', 'ICICI Bank', 'HCLTech',
                  'Tech Mahindra', 'Genpact', 'TP', 'Jio', 'Axis Bank', 'Concentrix Corporation', 'Amazon', 'Reliance Retail',
                  'iEnergizer', 'LTIMindtree', 'IBM'],
    'ratings': ['3.3', '3.7', '3.6', '3.7', '3.7', '3.8', '3.5', '4.0', '3.4', '3.4', '3.6', '3.8', '4.4', '3.6', '3.6',
                '3.9', '3.9', '4.6', '3.6', '3.9'],
    'domains': ['IT Services & Consulting', 'IT Services & Consulting', 'IT Services & Consulting', 'IT Services & Consulting',
                'IT Services & Consulting', 'Banking', 'IT Services & Consulting', 'Banking', 'IT Services & Consulting',
                'IT Services & Consulting', 'Analytics & KPO', 'BPO', 'Telecom', 'Banking', 'BPO', 'Internet', 'Retail',
                'BPO', 'IT Services & Consulting', 'IT Services & Consulting'],
    'reviews': ['1.1L', '72.9k', '64.7k', '61k', '52.7k', '51.8k', '48.4k', '45.6k', '45.6k', '43.1k', '41.8k', '37.9k',
                '33.6k', '32.9k', '32k', '31.4k', '27.3k', '27.2k', '26.2k', '25.7k'],
    'salaries': ['10L', '6.6L', '4.8L', '6L', '4.8L', '1.5L', '5.2L', '1.5L', '3.9L', '2.8L', '2.3L', '98k', '62k', '1L',
                 '1.3L', '1.5L', '76.8k', '24.6k', '2L', '2.2L'],
    'interviews': ['11.8k', '9.3k', '6.8k', '6.4k', '5.5k', '3k', '8.4k', '2.9k', '4.5k', '4.5k', '3.9k', '2.2k', '4.4k',
                   '1.9k', '2k', '5.9k', '1.9k', '1.4k', '3.4k', '2.6k'],
    'jobs': ['3.4k', '26.1k', '360', '475', '2.1k', '347', '2.6k', '12', '237', '621', '968', '1.4k', None, '206', '37',
             '2.3k', '100', '77', '420', '2.6k'],
    'benefits': ['10.6k', '6.7k', '4.6k', '5.5k', '3.7k', '3.2k', '4.8k', '3.7k', '3.8k', '3.4k', '3.5k', '1.8k', '2.5k',
                 '2.1k', '3.1k', '3.6k', '1.8k', '430', '777', '2.6k'],
    'photos': ['93', '49', '107', '92', '42', '86', '120', '73', '65', '79', '66', '38', '89', '121', '67', '91', '137', '29', '34', '23']
}

df = pd.DataFrame(data)

prof = ProfileReport(df)
prof.to_file(output_file='output.html')
print("Report saved as output.html")