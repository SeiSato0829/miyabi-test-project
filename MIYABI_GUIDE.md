# 🌸 Miyabi 完全使い方ガイド

## 目次
1. [Miyabiとは](#miyabiとは)
2. [セットアップ完了状況](#セットアップ完了状況)
3. [基本的な使い方](#基本的な使い方)
4. [コマンド一覧](#コマンド一覧)
5. [ワークフロー例](#ワークフロー例)
6. [トラブルシューティング](#トラブルシューティング)

---

## Miyabiとは

**GitHubをOSとして使う自律型AIエージェントシステム**

従来のClaude Codeの弱点（短期記憶、コンテキスト制限）を、GitHubのIssue・PR・Commitsを「永続的なメモリ」として活用することで克服した革命的なツールです。

### 主な特徴
- 🤖 **7つの自律型エージェント**が協力して開発
- 📝 **GitHub Issueに記憶を永続保存**
- 🔄 **1コマンドで全開発サイクル完了**
- 🚀 **大規模プロジェクト対応**

---

## セットアップ完了状況

✅ **インストール済み：**
- Ubuntu 24.04 LTS (WSL2)
- Git 2.43.0
- Node.js v20.19.3
- Rust 1.90.0
- GitHub CLI 2.62.0
- Miyabi 0.15.0

✅ **設定済み：**
- Anthropic API Key
- GitHub Token（設定済み）
- GitHubアカウント：SeiSato0829
- テストリポジトリ：miyabi-test-project

✅ **環境変数（~/.bashrc に追加済み）：**
```bash
export ANTHROPIC_API_KEY="sk-ant-api03-****"
export GITHUB_TOKEN="ghp_****"
export PATH="$HOME/.cargo/bin:$HOME/bin:$PATH"
```

---

## 基本的な使い方

### 1. 環境変数の読み込み（新しいターミナルを開いた時）

```bash
source ~/.bashrc
cd ~/miyabi-test-project
```

### 2. ステータス確認

```bash
miyabi status
```

### 3. 新しいタスクを作成（GitHubでIssueを作成）

```bash
gh issue create --title "タスクのタイトル" --body "詳細な説明"
```

### 4. Miyabiに自動実行させる

```bash
miyabi auto --issue <Issue番号>
```

例：
```bash
miyabi auto --issue 1
```

### 5. リアルタイム監視モード（Watch Mode）

```bash
miyabi status --watch
```

---

## コマンド一覧

### 基本コマンド

| コマンド | 説明 | 使用例 |
|---------|------|--------|
| `miyabi status` | プロジェクトの状態確認 | `miyabi status` |
| `miyabi status --watch` | リアルタイム監視（3秒ごと更新） | `miyabi status --watch` |
| `miyabi setup` | 初期セットアップ | `miyabi setup` |
| `miyabi --version` | バージョン確認 | `miyabi --version` |
| `miyabi --help` | ヘルプ表示 | `miyabi --help` |

### エージェント実行

| コマンド | 説明 | 使用例 |
|---------|------|--------|
| `miyabi auto --issue <N>` | Issue全自動実行 | `miyabi auto --issue 1` |
| `miyabi agent run coordinator --issue <N>` | Coordinatorのみ実行 | `miyabi agent run coordinator --issue 1` |
| `miyabi agent run codeGen --issue <N>` | CodeGenのみ実行 | `miyabi agent run codeGen --issue 1` |
| `miyabi agent run review --issue <N>` | Reviewのみ実行 | `miyabi agent run review --issue 1` |

### 並列実行

| コマンド | 説明 | 使用例 |
|---------|------|--------|
| `miyabi parallel --issues 1,2,3` | 複数Issueを並列実行 | `miyabi parallel --issues 1,2,3` |
| `miyabi parallel --issues 1,2,3 --concurrency 2` | 同時実行数を指定 | `miyabi parallel --issues 1,2,3 --concurrency 2` |

---

## ワークフロー例

### 例1: 新機能開発の完全自動化

```bash
# 1. 新機能のIssueを作成
gh issue create --title "ユーザー認証機能の追加" --body "JWT認証を実装してください"

# 2. Issue番号を確認（例: #2）
gh issue list

# 3. Miyabiに自動実行させる
miyabi auto --issue 2

# 4. リアルタイムで進捗確認
miyabi status --watch
```

**Miyabiが自動で実行：**
1. ✅ タスク分析（CoordinatorAgent）
2. ✅ 設計・計画作成
3. ✅ コード生成（CodeGenAgent）
4. ✅ テスト作成
5. ✅ コードレビュー（ReviewAgent）
6. ✅ Pull Request作成（PRAgent）
7. ✅ GitHubにプッシュ

### 例2: 複数のバグ修正を並列処理

```bash
# バグ修正Issue #3, #4, #5を同時に処理
miyabi parallel --issues 3,4,5 --concurrency 3
```

### 例3: 段階的な実行（手動制御）

```bash
# ステップ1: まず計画だけ作成
miyabi agent run coordinator --issue 6

# ステップ2: 計画を確認してからコード生成
gh issue view 6  # 計画を確認
miyabi agent run codeGen --issue 6

# ステップ3: レビュー実行
miyabi agent run review --issue 6

# ステップ4: PR作成
miyabi agent run pr --issue 6
```

---

## 7つのエージェント詳細

### 1. CoordinatorAgent（調整役）
- **役割**: タスク分析・分解・計画立案
- **実装言語**: TypeScript/Rust
- **優先度**: High

### 2. IssueAgent（Issue管理）
- **役割**: Issueの作成・更新・ラベル管理
- **実装言語**: TypeScript/Rust
- **優先度**: High

### 3. CodeGenAgent（コード生成）
- **役割**: 実装コード・テストコードの生成
- **実装言語**: TypeScript/Rust
- **優先度**: High

### 4. ReviewAgent（品質保証）
- **役割**: コードレビュー・静的解析・テスト実行
- **実装言語**: TypeScript/Rust
- **優先度**: Medium

### 5. PRAgent（Pull Request管理）
- **役割**: PR作成・マージ管理
- **実装言語**: TypeScript/Rust
- **優先度**: Medium

### 6. DeploymentAgent（デプロイ）
- **役割**: デプロイ実行（デフォルト無効）
- **実装言語**: TypeScript/Rust
- **優先度**: Low

### 7. MonitoringAgent（監視）
- **役割**: パフォーマンス監視・エラー検知
- **実装言語**: TypeScript/Rust
- **優先度**: Low

---

## 設定ファイル（.miyabi.yml）

プロジェクトルートの`.miyabi.yml`で動作をカスタマイズできます：

```yaml
# GitHub Settings
github:
  owner: SeiSato0829
  repo: miyabi-test-project
  defaultBranch: main

# Claude Model Settings
claude:
  model: claude-3-5-sonnet-20241022
  maxTokens: 4096
  temperature: 0.7

# Agent Settings
agents:
  coordinator:
    enabled: true
    priority: high

  codeGen:
    enabled: true
    priority: high

  review:
    enabled: true
    priority: medium

  pr:
    enabled: true
    priority: medium

  deployment:
    enabled: false  # デプロイは手動で有効化
    priority: low

# Execution Settings
execution:
  maxRetries: 3
  timeout: 300000
  parallel:
    enabled: true
    maxConcurrency: 3

# Feature Flags
features:
  autoMerge: false      # 自動マージは慎重に
  autoDeploy: false     # 自動デプロイは慎重に
  notifyOnComplete: true
```

---

## トラブルシューティング

### 問題1: `miyabi: command not found`

**原因**: PATHが設定されていない

**解決策**:
```bash
source ~/.bashrc
# または
export PATH="$HOME/.nvm/versions/node/v20.19.3/bin:$PATH"
```

### 問題2: `GITHUB_TOKEN not found`

**原因**: 環境変数が設定されていない

**解決策**:
```bash
export GITHUB_TOKEN="ghp_YOUR_TOKEN_HERE"
# または
source ~/.bashrc
```

### 問題3: `ANTHROPIC_API_KEY not found`

**原因**: API Keyが設定されていない

**解決策**:
```bash
export ANTHROPIC_API_KEY="sk-ant-api03-nRn..."
# または
source ~/.bashrc
```

### 問題4: API制限エラー（`Approaching weekly limit`）

**原因**: ClaudeのAPI使用量が週間制限に達した

**解決策**:
- 無料枠：週5ドル → 有料プランにアップグレード
- または翌週まで待機

### 問題5: GitHub権限エラー（`Missing required token scopes`）

**原因**: GitHubトークンに必要な権限がない

**解決策**:
```bash
gh auth refresh -h github.com -s read:org,repo,workflow
```

### 問題6: エージェントが動かない

**チェックリスト**:
1. ✅ `miyabi status` が正常に動作するか確認
2. ✅ Issueが正しく作成されているか確認（`gh issue list`）
3. ✅ `.miyabi.yml` の設定を確認
4. ✅ ログを確認（`cat miyabi.log`）

---

## 便利なTips

### Tip 1: 環境変数を毎回設定しなくて済むようにする

`~/.bashrc`に以下を追加済みなので、新しいターミナルでは自動設定されます：
```bash
export ANTHROPIC_API_KEY="sk-ant-api03-****"
export GITHUB_TOKEN="ghp_****"
export PATH="$HOME/.cargo/bin:$HOME/bin:$PATH"
```

### Tip 2: Issue作成のテンプレート化

よく使うIssueの形式をテンプレート化：
```bash
# エイリアス作成
echo 'alias miyabi-bug="gh issue create --label bug --title"' >> ~/.bashrc
echo 'alias miyabi-feature="gh issue create --label enhancement --title"' >> ~/.bashrc

# 使い方
miyabi-bug "ボタンが動かない" --body "詳細..."
miyabi-feature "新機能追加" --body "詳細..."
```

### Tip 3: GitHubでの確認

ブラウザでプロジェクトを確認：
```bash
gh repo view --web
```

特定のIssueを確認：
```bash
gh issue view 1 --web
```

### Tip 4: ログの確認

```bash
# リアルタイムログ監視
tail -f ~/miyabi-test-project/miyabi.log

# エラーのみ抽出
grep ERROR ~/miyabi-test-project/miyabi.log
```

---

## 次のステップ

1. **実際のプロジェクトで試す**
   ```bash
   cd your-project
   miyabi setup
   ```

2. **より複雑なタスクに挑戦**
   - マイクロサービスの構築
   - フルスタックアプリの開発
   - データベース設計と実装

3. **Rust版にアップグレード（将来）**
   - パフォーマンスが50%向上
   - メモリ使用量が50%削減

4. **コミュニティに参加**
   - Discord: https://discord.gg/Urx8547abS
   - GitHub: https://github.com/ShunsukeHayashi/Miyabi

---

## 参考リンク

- [Miyabi公式リポジトリ](https://github.com/ShunsukeHayashi/Miyabi)
- [リリースノート v0.1.1](https://github.com/ShunsukeHayashi/Miyabi/releases/tag/v0.1.1)
- [トラブルシューティング](https://github.com/ShunsukeHayashi/Miyabi/blob/main/docs/TROUBLESHOOTING.md)
- [Getting Started](https://github.com/ShunsukeHayashi/Miyabi/blob/main/docs/GETTING_STARTED.md)

---

## まとめ

Miyabiを使えば：
- ✅ **1コマンドで全開発サイクルが完了**
- ✅ **GitHubが記憶装置として機能**
- ✅ **複数タスクの並列処理が可能**
- ✅ **大規模プロジェクトに対応**
- ✅ **AIの真の力を引き出せる**

**あなたはもうMiyabiマスターです！**

---

作成日: 2025年10月20日
バージョン: Miyabi 0.15.0
プロジェクト: miyabi-test-project
