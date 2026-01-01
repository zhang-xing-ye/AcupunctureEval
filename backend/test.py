import sys
import os

# 修正后的导入方式，基于backend作为根目录
from dao.qa_leaderboard_dao import get_all_sorted_by_score
from dao.vqa_leaderboard_dao import get_all_sorted_by_score as get_vqa_records
from core.database import SessionLocal

def test_get_all_sorted_by_score():
    db = SessionLocal()
    try:
        print("Fetching all QA Leaderboard records...")
        records = get_all_sorted_by_score(db)
        
        if not records:
            print("No records found.")
            return

        print(f"Found {len(records)} records.")
        print("-" * 120)
        print(f"{'ID':<5} | {'LLM Name':<30} | {'Org':<10} | {'Avg':<6} | {'A1':<6} | {'A2':<6} | {'A3':<6} | {'A4':<6} | {'B':<6} | {'X':<6}")
        print("-" * 120)
        
        for r in records:
            print(f"{r.id:<5} | {r.llm_name:<30} | {r.llm_org:<10} | {r.avg_score:<6} | {r.a1_score:<6} | {r.a2_score:<6} | {r.a3_score:<6} | {r.a4_score:<6} | {r.b_score:<6} | {r.x_score:<6}")
            
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        db.close()

def test_get_vqa_records():
    db = SessionLocal()
    try:
        print("Fetching all VQA Leaderboard records...")
        records = get_vqa_records(db)
        
        if not records:
            print("No records found.")
            return

        print(f"Found {len(records)} records.")
        print("-" * 120)
        print(f"{'ID':<5} | {'LLM Name':<30} | {'T1 Single':<10} | {'T1 Multi':<10} | {'T2':<10} | {'T3':<10} | {'Avg':<10}")
        print("-" * 120)
        
        for r in records:
            print(f"{r.id:<5} | {r.llm_name:<30} | {r.type_one_single_score:<10} | {r.type_one_multi_score:<10} | {r.type_two_score:<10} | {r.type_three_score:<10} | {r.avg_score:<10}")
            
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    # test_get_all_sorted_by_score()
    test_get_vqa_records()
