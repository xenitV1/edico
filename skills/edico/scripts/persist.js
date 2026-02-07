const fs = require('fs');
const path = require('path');
const os = require('os');

/**
 * Persists synthesized research data to a JSONL file in the user's home directory.
 */
function persistData() {
    const args = process.argv.slice(2);
    const params = {};

    for (let i = 0; i < args.length; i += 2) {
        if (!args[i]) break;
        const key = args[i].replace('--', '');
        const value = args[i + 1];
        params[key] = value;
    }

    // analysis is the new summary, representing exhaustive research
    const { topic, analysis, sources, tags, timestamp } = params;

    if (!topic || !analysis) {
        console.error('Error: --topic and --analysis are required.');
        process.exit(1);
    }

    const homeDir = os.homedir();
    const webdataDir = path.join(homeDir, '.webdata');
    const logFile = path.join(webdataDir, 'research_log.jsonl');

    // Ensure directory exists
    if (!fs.existsSync(webdataDir)) {
        fs.mkdirSync(webdataDir, { recursive: true });
        console.log(`Created directory: ${webdataDir}`);
    }

    const data = {
        timestamp: timestamp || new Date().toISOString(),
        topic,
        detailed_analysis: analysis,
        sources: sources ? sources.split(',').map(s => s.trim()) : [],
        tags: tags ? tags.split(',').map(t => t.trim()) : []
    };

    try {
        fs.appendFileSync(logFile, JSON.stringify(data) + '\n', 'utf8');
        console.log(`Successfully persisted data to ${logFile}`);
    } catch (err) {
        console.error(`Error persisting data: ${err.message}`);
        process.exit(1);
    }
}

persistData();
