# Let's check the complete dataset to ensure we include ALL data
print(f"Total students: {len(df)}")

# Check for any missing values
print("\nMissing values:")
print(df.isnull().sum())

# Check the range of student codes and ranks
print(f"\nStudent code range: {df['كود الطالب'].min()} to {df['كود الطالب'].max()}")
print(f"Rank range: {df['الترتيب'].min()} to {df['الترتيب'].max()}")
print(f"Grade range: {df['الدرجة'].min()} to {df['الدرجة'].max()}")

# Check for any duplicate student codes
duplicate_codes = df['كود الطالب'].duplicated().sum()
print(f"Duplicate student codes: {duplicate_codes}")

# Prepare the data for the website
student_data = df.copy()
student_data = student_data.rename(columns={
    'الترتيب': 'rank',
    'كود الطالب': 'student_code', 
    'الأسم': 'name',
    'الدرجة': 'grade'
})

print("\nSample of prepared data:")
print(student_data.head(10))